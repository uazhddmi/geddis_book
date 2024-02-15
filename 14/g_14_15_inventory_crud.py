import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
QUIT = 5


def main():
    choice = 0
    while choice != QUIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()


def display_menu():
    print('\n------Inventory menu------')
    print('1. Create new item. ')
    print('2. Read item. ')
    print('3. Update item. ')
    print('4. Delete item. ')
    print('5. Exit. ')


def get_menu_choice():
    choice = int(input('Enter your choice: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Accepted values are {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))

    return choice


def create():
    print('Create new position')
    name = input('Item name: ')
    price = float(input('Item price: '))
    insert_row(name, price)


def read():
    name = input('Enter Item\'s name you are looking for. ')
    num_found = display_item(name)
    print(f'{num_found} row(s) have found')


def update():
    read()

    selected_id = int(input('Choose Id of position you want to update. '))

    name = input('Enter new name of Item: ')
    price = input('Enter updated price: ')
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} rows were updated')


def delete():
    read()
    selected_id = int(input('Enter ID of position you want to delete. '))

    sure = input('Are you sure you want to delete? y/n ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} rows were deleted.')


def insert_row(name, price):
    conn = None

    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?)''',
                    (name, price))
        conn.commit()

    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn is not None:
            conn.close()


def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                    WHERE ItemName == ?''',
                    (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15} Price: {row[2]: <6}')
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn is not None:
            conn.close()
    return len(results)


def update_row(uid, id_name, price):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                SET ItemName = ?, Price = ?
                WHERE ItemID == ?''',
                    (id_name, price, uid))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn is not None:
            conn.close()

    return num_updated


def delete_row(uid):
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory
                    WHERE ItemId == ?''',
                    (uid,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn is not None:
            conn.close()
            return num_deleted


if __name__ == '__main__':
    main()
