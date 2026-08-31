"""
Talking to Google Firestore -- a cloud NoSQL database -- from Python with the
Firebase Admin SDK. Where sqlite stores rows in tables, Firestore stores
JSON-like documents inside collections: collections -> documents -> fields.
There are no schemas, no tables, and no JOINs.

Before running this script:
  1. In the Firebase console, create a project and a Firestore database.
  2. Create a service account and download its key as service_key.json,
     saved beside this file. Never commit that key (it is gitignored).
  3. Install the SDK:  pip install firebase-admin

This script runs one full create -> read -> update -> delete cycle.
"""

import firebase_admin
from firebase_admin import credentials, firestore


def get_client(key_path: str = 'service_key.json') -> firestore.Client:
    """
    Initialize the Firebase Admin app once and return a Firestore client.

    :param key_path: the path to a Firebase service-account key file
    :precondition: key_path names a readable Firebase service-account JSON key
    :postcondition: the default Firebase Admin app is initialized if it was not
                     already
    :return: a Firestore client connected to the project named by the key
    """
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(credentials.Certificate(key_path))
    return firestore.client()


def add_student(database: firestore.Client, name: str,
                score: int) -> str:
    """
    Add one student document to the "students" collection.

    :param database: a Firestore client
    :param name: the student's name
    :param score: the student's score
    :precondition: database is a Firestore client
    :precondition: name is a string and score is an int
    :postcondition: one new document is added to the "students" collection
    :return: the auto-generated id of the new document
    """
    document_reference = database.collection('students').document()
    document_reference.set({'name': name, 'score': score})
    return document_reference.id


def get_students(database: firestore.Client) -> list:
    """
    Read every document in the "students" collection.

    :param database: a Firestore client
    :precondition: database is a Firestore client
    :postcondition: the "students" collection is unchanged
    :return: a list of (document_id, fields) tuples, where fields is a dict
    """
    return [(document.id, document.to_dict())
            for document in database.collection('students').stream()]


def update_score(database: firestore.Client, document_id: str,
                 new_score: int) -> None:
    """
    Change one student's score, leaving the rest of the document untouched.

    :param database: a Firestore client
    :param document_id: the id of the document to update
    :param new_score: the replacement score
    :precondition: database is a Firestore client
    :precondition: document_id names an existing document in "students"
    :precondition: new_score is an int
    :postcondition: that document's "score" field is set to new_score
    :return: None
    """
    database.collection('students').document(document_id).update(
        {'score': new_score})


def delete_student(database: firestore.Client,
                   document_id: str) -> None:
    """
    Delete one student document.

    :param database: a Firestore client
    :param document_id: the id of the document to delete
    :precondition: database is a Firestore client
    :precondition: document_id names a document in "students"
    :postcondition: that document no longer exists in "students"
    :return: None
    """
    database.collection('students').document(document_id).delete()


def format_student(document_id: str, fields: dict) -> str:
    """
    Build a one-line summary of a student document for printing.

    :param document_id: a Firestore document id
    :param fields: the document's fields as a dict with "name" and "score"
    :precondition: document_id is a non-empty string
    :precondition: fields is a dict with a "name" string and a "score" int
    :postcondition: document_id and fields are unchanged
    :return: a one-line string "<id>: <name> scored <score>"

    >>> format_student('A1B2', {'name': 'Chris', 'score': 91})
    'A1B2: Chris scored 91'
    >>> format_student('F9D4', {'name': 'Alex', 'score': 87})
    'F9D4: Alex scored 87'
    """
    return f'{document_id}: {fields["name"]} scored {fields["score"]}'


def main():
    """
    Drive the program.
    """
    try:
        database = get_client()
        new_id = add_student(database, 'Chris', 91)
        print(f'Created document {new_id}')

        print('All students:')
        for document_id, fields in get_students(database):
            print(' ', format_student(document_id, fields))

        update_score(database, new_id, 95)
        print(f'Updated {new_id} to score 95')

        delete_student(database, new_id)
        print(f'Deleted {new_id}')
    except Exception as error:  # What is wrong with this and why is it wrong?
        # Network, permission, and missing-key problems all surface here.
        print('Firestore error:', error)


if __name__ == '__main__':
    main()
