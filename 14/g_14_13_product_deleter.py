import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    pid = int(input('Enter product ID to delete: '))

    cur.execute('''SELECT Description FROM Products
                WHERE ItemID == ?''', (pid,))
    results = cur.fetchone()

    if results is not None:
        sure = input(f'Are you sure you want to delete {results[0]}? (y/n)')
        if sure.lower() == 'y':
            cur.execute('''DELETE FROM Products 
                        WHERE ItemID == ?''', (pid,))

        conn.commit()
        print('Item was deleted,', f'{cur.rowcount} was deleted from base')
    else:
        print(f'Product with {pid} ID wasn\'t found.')

    conn.close()


if __name__ == '__main__':
    main()
