"""
Now let's put some rows into the table we created.
"""

import sqlite3


def create_students_table(connection: sqlite3.Connection) -> None:
    """
    Create the students table if it does not already exist.

    :param connection: an open sqlite3 connection
    :precondition: connection is an open sqlite3 connection
    :postcondition: connection is unchanged
    :postcondition: a "students" table exists, with columns id (integer
                     primary key), name (text), and grade (integer)
    :return: None
    """
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    ''')
    connection.commit()


def insert_students(connection: sqlite3.Connection,
                    students: list) -> None:
    """
    Insert a batch of (name, grade) rows into the students table.

    :param connection: an open sqlite3 connection
    :param students: a list of (name, grade) tuples
    :precondition: connection is an open sqlite3 connection with a
                    students table
    :precondition: students is a list of (str, int) tuples
    :postcondition: students is unchanged
    :postcondition: one row is added to the students table per entry in
                     students
    :return: None

    >>> db = sqlite3.connect(':memory:')
    >>> create_students_table(db)
    >>> insert_students(db, [('Amy', 91), ('Bo', 78)])
    >>> db.execute('SELECT name, grade FROM students').fetchall()
    [('Amy', 91), ('Bo', 78)]
    >>> db.close()
    """
    connection.executemany(
        'INSERT INTO students (name, grade) VALUES (?, ?)', students)
    connection.commit()


def main():
    """
    Drive the program.
    """
    connection = sqlite3.connect('codebench.db')
    create_students_table(connection)

    # Clear old demo rows first, so re-running this file gives the same
    # result every time instead of piling up duplicates.
    connection.execute('DELETE FROM students')
    connection.commit()

    students = [('Amy', 91), ('Bo', 78), ('Genevieve', 85)]
    insert_students(connection, students)
    print(f'Inserted {len(students)} students.')
    connection.close()


if __name__ == '__main__':
    main()
