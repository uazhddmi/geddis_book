import sqlite3


def main():
    again = 'y'

    while again == 'y':
        item_id = int(input('ID of '))
        item_name = input('Item name: ')
        price = float(input('Price: '))

        add_item(item_id, item_name, price)

        again = input('Add one more position? y/n: ')


def add_item(item_id, item_name, price):
    conn = None

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                        VALUES (?, ?, ?)''',
                    (item_id, item_name, price))
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()


