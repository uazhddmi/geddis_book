import  sqlite3


def main():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()

        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''
                    SELECT
                        Employees.Name,
                        Departments.DepartmentName,
                        Locations.City
                    FROM
                        Employees, Departments, Locations
                    WHERE
                        Employees.DepartmentID == Departments.DepartmentID AND
                        Employees.LocationID == Locations.LocationID''')
        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:15} {row[1]:25} {row[2]}')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()