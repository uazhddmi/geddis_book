import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    pid = int(input('Enter your product ID: '))

    cur.execute('''SELECT Description, RetailPrice FROM Products
                WHERE ItemID == ?''', (pid,))
    results = cur.fetchone()

    if results is not None:
        print(f'Current price for {results[0]}:'
              f'${results[1]:.2f}')
        new_price = float(input('Enter new price: '))

        cur.execute('''UPDATE Products 
                    SET RetailPrice = ?
                    WHERE ItemID == ?''', (new_price, pid))

        conn.commit()
        print('Price was updated')
    else:
        print(f'Product with {pid} ID wasn\'t found.')

    conn.close()


if __name__ == '__main__':
    main()
