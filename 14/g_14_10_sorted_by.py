import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    cur.execute('''SELECT Description, RetailPrice FROM Products
                ORDER BY RetailPrice''')  # Descending order with DESC after RetailPrice

    results = cur.fetchall()

    for row in results:
        print(f'{row[0]:35} {row[1]:5}')

    conn.close()


if __name__ == '__main__':
    main()