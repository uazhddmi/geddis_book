import sqlite3


def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Here goes code for communication with database

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
