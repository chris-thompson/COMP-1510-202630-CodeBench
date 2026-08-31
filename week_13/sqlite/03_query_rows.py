"""
Finally, let's ask the database questions with SELECT.
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
    """
    connection.executemany(
        'INSERT INTO students (name, grade) VALUES (?, ?)', students)
    connection.commit()


def students_with_grade_at_least(connection: sqlite3.Connection,
                                 minimum_grade: int) -> list:
    """
    Find every student with a grade at or above a minimum.

    :param connection: an open sqlite3 connection with a students table
    :param minimum_grade: an int
    :precondition: connection is an open sqlite3 connection with a
                    students table
    :precondition: minimum_grade is an int
    :postcondition: connection is unchanged
    :postcondition: minimum_grade is unchanged
    :return: a list of (name, grade) tuples, ordered by grade descending

    >>> db = sqlite3.connect(':memory:')
    >>> create_students_table(db)
    >>> insert_students(db, [('Amy', 91), ('Bo', 78), ('Genevieve', 85)])
    >>> students_with_grade_at_least(db, 80)
    [('Amy', 91), ('Genevieve', 85)]
    >>> students_with_grade_at_least(db, 100)
    []
    >>> db.close()
    """
    cursor = connection.execute(
        'SELECT name, grade FROM students '
        'WHERE grade >= ? ORDER BY grade DESC',
        (minimum_grade,))
    return cursor.fetchall()


def main():
    """
    Drive the program.
    """
    connection = sqlite3.connect('codebench.db')
    create_students_table(connection)
    connection.execute('DELETE FROM students')
    connection.commit()
    insert_students(connection, [('Amy', 91), ('Bo', 78), ('Genevieve', 85)])

    print('Every student, highest grade first:')
    for name, grade in students_with_grade_at_least(connection, 0):
        print(f'  {name}: {grade}')

    print('\nStudents with a grade of at least 85:')
    for name, grade in students_with_grade_at_least(connection, 85):
        print(f'  {name}: {grade}')

    connection.close()


if __name__ == '__main__':
    main()
