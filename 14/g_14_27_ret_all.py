import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM Products
                WHERE RetailPrice > 7.0
                ORDER BY RetailPrice''')

    results = cur.fetchall()

    for row in results:
        print(*row, sep='---')

    conn.close()


if __name__ == '__main__':
    main()
