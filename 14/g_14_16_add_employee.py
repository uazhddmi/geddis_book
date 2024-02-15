import sqlite3


def main():
    conn = None
    try:
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''INSERT INTO Employees
                                    (Name, Position, DepartmentID, LocationID)
                            VALUES ('Djanel Grant', 'Engineer', 2, 1),
                                    ('Jack Smith', 'Manager', 3, 3),
                                    ('Sonya Alyadero', 'Revisor', 1, 2),
                                    ('Rene Kinneid', 'Designer', 3, 3),
                                    ('Arlin Meyers', 'Supervisor', 4, 4)
                            ''')
        conn.commit()

        print('Employee successfully added')

    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()