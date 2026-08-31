"""
sqlite3 ships with Python: no install required. A "connection" is a
handle to a database file (or to memory); a "cursor" runs SQL through it.
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

    >>> db = sqlite3.connect(':memory:')
    >>> create_students_table(db)
    >>> query = "SELECT name FROM sqlite_master WHERE type='table'"
    >>> db.execute(query).fetchall()
    [('students',)]
    >>> db.close()
    """
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    ''')
    connection.commit()


def main():
    """
    Drive the program.
    """
    connection = sqlite3.connect('codebench.db')
    create_students_table(connection)
    print('Connected to codebench.db and ensured the students table exists.')
    connection.close()


if __name__ == '__main__':
    main()
