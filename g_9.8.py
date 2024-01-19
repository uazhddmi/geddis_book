import pickle
import sys


def open_file(file: str):
    '''
    Converts .dat file to dictionary
    '''
    with open(file, 'rb') as sors:
        return pickle.load(sors)


def menu():
    choice = 0
    while choice < 1 or choice > 5:
        print("People and their e-mails")
        print("1. Find e-mail")
        print("2. Add e-mail")
        print("3. Edit e-mail")
        print("4. Delete e-mail")
        print("5. If you want to exit")
        try:
            choice = int(input('Please, choose what you want to do. '))
        except ValueError:
            print('You entered wrong value, should be from 1 to 5')
            choice = 0


    return choice

def search_email(emails_dict: dict):
    proceed = ''
    while proceed == '':
        us_name = input('Please, enter name you want to find. ')
        print(emails_dict.get(us_name, "There is no such user"))
        futher_proceed(emails_dict)


def futher_proceed(emails_dict):
    proceed = input('If you want to proceed one more time press \'Enter\'.\n'
                    'If you want go back to menu press "m".\n'
                    'If you want exit press "q"')

    if proceed == '':
        return proceed
    elif proceed.lower() == 'm':
        write_file(emails_dict)
        main()
    elif 'q' in proceed.lower():
        write_file(emails_dict)
        sys.exit()

    else:
        print('Please, make right choise')

def add_email(emails_dict: dict):
    proceed = ''
    while proceed == '':
        us_name = input('Please, enter name you want to add. ')
        if us_name in emails_dict:
            print('Already in the dict')
        else:
            emails_dict[us_name] = input('Please, enter corresponding e-mail')
        futher_proceed(emails_dict)


def edit_email(emails_dict: dict):
    proceed = ''
    while proceed == '':
        us_name = input('Please, enter name you want to update. ')
        print(f'Present value for {us_name} is {emails_dict[us_name]}')
        emails_dict[us_name] = input('Enter updated e-mail')
        print(f'Updated value for {us_name} is {emails_dict[us_name]}')
        futher_proceed(emails_dict)


def del_email(emails_dict: dict):
    proceed = ''
    while proceed == '':
        us_name = input('Please, enter name you want to delete. ')
        confirm = input(f'User {us_name} with e-mail {emails_dict[us_name]} will be deleted.\n'
                         'If you confirm delition press "y"\n'
                         'If you want to decline operation hit "Enter"')
        if confirm.lower() == 'y':
            emails_dict.pop(us_name, "There no such name in a list")

        futher_proceed(emails_dict)


def write_file(emais_dict: dict):
    with open('emails.dat', 'wb') as output:
        pickle.dump(emais_dict, output)

def main():
    emails_dict = open_file('emails.dat')
    print(emails_dict)
    us_choice = menu()

    if us_choice == 5:
        write_file(emails_dict)
        sys.exit()
    elif us_choice == 1:
        search_email(emails_dict)
    elif us_choice == 2:
        add_email(emails_dict)
    elif us_choice == 3:
        edit_email(emails_dict)
    elif us_choice == 4:
        del_email(emails_dict)
    else:
        print('This message shouldn\'t appear')


if __name__ == '__main__':
    main()