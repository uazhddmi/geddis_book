import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Products (ItemID INTEGER PRIMARY KEY NOT NULL,
                                                        Description  TEXT,
                                                        RetailPrice REAL)''')
    conn.commit()
    again = 'y'
    while again == 'y':
        desc = input('Description: ')
        ret_pr = float(input('Retail Price: '))
        cur.execute('''INSERT INTO Products (Description, RetailPrice)
                    VALUES(?, ?)''', (desc, ret_pr))
        conn.commit()
        again = input("Add one more, y/n")

    cur.execute('SELECT Description, RetailPrice FROM Products')

    results = cur.fetchall()

    for row in results:
        print(f'{row[0]:35} {row[1]:5}')

    conn.close()


if __name__ == '__main__':
    main()
