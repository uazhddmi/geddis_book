import sqlite3
import sys


#  Create & connect to database & create table Entry
def db_create():
    conn = sqlite3.connect('students_info.db')
    cur = conn.cursor()
    #  CREATE table for Majors, Departments, Students
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors(MajorID INTEGER PRIMAY KEY,
                                                    Name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Departments(DeptID INTEGER PRIMAY KEY,
                                                    Name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Students(StudentID INTEGER PRIMAY KEY,
                                                    Name TEXT, 
                                                    MajorID 
                                                    DeptID )''')
    conn.commit()
    conn.close()


def work_with_Students():
    pass


def work_with_Majors():
    pass


def work_with_Departments():
    pass


def main():
    conn, cur = db_connect('students_info.db')
    choosing_table()


def choosing_table():
    main_menu()
    choice = 0
    while choice < 1 or choice > 5:
        choice = int(input('>'))
    if choice == 1:
        work_with_Students()
    elif choice == 2:
        work_with_Majors()
    elif choice == 3:
        work_with_Departments()
    elif choice == 4:
        sys.exit()
    else:
        raise Exception('SOME UNATTENDED BEHAVIOUR')

def main_menu():
    print('Please, choose which table do you want to operate.')
    print('-' * 50)
    print('1. Students')
    print('2. Majors')
    print('3. Departments')
    print('4. Quit')

def db_connect(db_file=None):
    conn = sqlite3.connect(db_file)
    return conn, conn.cursor()


if __name__ == '__main__':
    main()