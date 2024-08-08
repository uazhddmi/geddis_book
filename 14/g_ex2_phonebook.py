import sqlite3
import sys


#  Create & connect to database & create table Entry
def db_create():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    #  CREATE table for cities
    cur.execute('''CREATE TABLE IF NOT EXISTS Entry(Name TEXT NOT NULL,
                                                    Number INTEGER NOT NULL)''')
    conn.commit()
    conn.close()


def db_connect(db_file=None):
    conn = sqlite3.connect('phonebook.db')
    return conn, conn.cursor()


#  Create menu
def menu():
    print('Please, choose what you want to do.')
    print('-' * 50)
    print('1. Search for contact')
    print('2. Edit contact\'s data')
    print('3. Add contact')
    print('4. Delete contact')
    print('5. Quit')


def user_choice():
    menu()
    choice = 0
    while choice < 1 or choice > 5:
        choice = int(input('>'))
    if choice == 1:
        find_con()
    elif choice == 2:
        edit_con()
    elif choice == 3:
        create_con()
    elif choice == 4:
        delete_con()
    elif choice == 5:
        conn, *_ = db_connect()
        conn.close()
        sys.exit()


#  Create entry to db
def create_con():
    conn, cur = db_connect()
    name = input('Enter name you want to add: ')
    number = int(input('Enter number for this contact: '))
    cur.execute('''INSERT INTO Entry(Name, Number)
                        VALUES (?, ?)''', (name, number))
    query = input(f'Name {name} with number {number} is going to be add to db.'
                  f'Is everything correct? Make record to db? y/n ')
    if 'y' in query.lower():
        conn.commit()
    else:
        conn.close()
        create_con()
    query = input('Do you want search one more time? y/n ')
    if 'y' in query.lower():
        create_con()
    else:
        main()


#  Find entry from db
def find_con():
    *_, cur = db_connect()
    name = input('Enter name you want to find: ')
    cur.execute('''SELECT RowID, Name, Number FROM Entry
                    WHERE Name == ?''', (name,))
    results = cur.fetchall()

    if results:
        for result in results:
            print(f'{result[0]} Name {result[1]} with number {result[2]} found in db')
    else:
        print('Such name wasn\'t found in db')
    query = input('Do you want search one more time? y/n ')
    if 'y' in query.lower():
        find_con()
    else:
        main()


#  Edit entry from db
def edit_con():
    conn, cur = db_connect()
    uid = int(input('Enter user ID you want to edit: '))
    name = input('Enter name you want to update: ')
    number = int(input('Enter updated number for this contact: '))
    cur.execute('''UPDATE Entry
                        SET Name == ?,
                            Number == ?
                        WHERE RowID == ?''', (name, number, uid))

    query = input(f'Name {name} with number {number} is going to be updated.'
                  f'Is everything correct? Make record to db? y/n ')
    if 'y' in query.lower():
        conn.commit()
    else:
        conn.close()
        edit_con()
    query = input('Do you want update one more contact? y/n ')
    if 'y' in query.lower():
        edit_con()
    else:
        main()


#  Delete entry from db
def delete_con():
    conn, cur = db_connect()
    uid = int(input('Enter user ID you want to edit: '))
    # name = input('Enter name you want to update: ')
    # number = int(input('Enter updated number for this contact: '))

    cur.execute('''SELECT Name, Number FROM Entry
                                WHERE RowID == ?''', (uid,))
    results = cur.fetchall()
    for result in results:
        name, number = result[0], result[1]

    query = input(f'Name {name} with number {number} is going to be deleted.'
                  f'Is everything correct? Make record to db? y/n ')
    if 'y' in query.lower():
        cur.execute('''DELETE FROM Entry
                                    WHERE RowID == ?''', (uid,))
        conn.commit()
    else:
        conn.close()
        delete_con()
    query = input('Do you want delete one more contact? y/n ')
    if 'y' in query.lower():
        delete_con()
    else:
        main()


def main():
    user_choice()


if __name__ == '__main__':
    main()
