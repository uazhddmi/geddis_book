import sqlite3


def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Add table INventory
    cur.execute('''CREATE TABLE (ItemID INTEGER PRIMARY KEY NOT NULL,
                ItemName TEXT, 
                Price REAL)''')

    # Add table Employees.
    cur.execute('''CREATE TABLE Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT,
                Position TEXT''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    