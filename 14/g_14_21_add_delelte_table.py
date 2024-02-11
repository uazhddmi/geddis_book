import sqlite3


def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Add table INventory
    cur.execute('''CREATE TABLE IF NOT EXISTS Book (ItemID INTEGER PRIMARY KEY NOT NULL,
                PublisherName TEXT,
                AuthorName TEXT,
                PageQuant REAL,
                ISBN_num REAL)''')

    cur.execute('''DROP TABLE IF EXISTS Book''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    