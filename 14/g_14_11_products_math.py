import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    cur.execute('''SELECT MIN(RetailPrice) FROM Products''')
    lowest = cur.fetchone()[0]

    cur.execute('''SELECT MAX(RetailPrice) FROM Products''')
    highest = cur.fetchone()[0]

    cur.execute('''SELECT AVG(RetailPrice) FROM Products''')
    average = cur.fetchone()[0]

    conn.close()

    print(f'Minimal price: ${lowest}')
    print(f'Maximal price: ${highest}')
    print(f'Average price: ${average:0.2f}')

if __name__ == '__main__':
    main()