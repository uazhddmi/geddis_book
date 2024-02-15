import sqlite3


def main():
    again = 'y'

    while again == 'y':
        # item_id = int(input('ID of '))
        item_name = input('Item name: ')
        price = float(input('Price: '))

        add_item(item_name, price)

        again = input('Add one more position? y/n: ')


def add_item(item_name, price):
    conn = None

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        #
        # cur.execute('''CREATE  TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
        #                                                                     ItemName TEXT NOT NULL,
        #                                                                     Price REAL NOT NULL''')

        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?)''',
                    (item_name, price))
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()


