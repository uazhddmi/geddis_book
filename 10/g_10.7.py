import pickle
import sys
import employee

def open_file(file: str):
    '''
    Converts .dat file to dictionary
    '''
    try:
        with open(file, 'rb') as sors:
            return pickle.load(sors)
    except IOError:
            return {}


def menu():
    choice = 0
    while choice < 1 or choice > 5:
        print("User information by their ID")
        print('_'*40)
        print("1. Find user by ID")
        print("2. Add user information")
        print("3. Edit user information")
        print("4. Delete user information")
        print("5. If you want to exit")
        try:
            choice = int(input('Please, choose what you want to do.\n'))
        except ValueError:
            print('You entered wrong value, should be from 1 to 5')
            choice = 0


    return choice

def search_user_info(emails_dict: dict):
    proceed = ''
    while proceed == '':
        user_id = input('Please, enter ID you want to find. ')
        print(emails_dict.get(user_id, "There is no such user"))
        futher_proceed(emails_dict)


def futher_proceed(emails_dict):
    proceed = input('If you want to proceed one more time press "Enter".\n'
                    'If you want go back to menu press "m".\n'
                    'If you want exit press "q"\t')

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

def add_user_info(emails_dict: dict):
    proceed = ''
    while proceed == '':
        id = input('Please, enter ID you want to add. ')
        if id in emails_dict:
            print('Already in the dict')
        else:
            emails_dict[id] = employee.Employee(id, input('Please, enter name. '),
                                                input('Please, enter department. '),
                                                input('Please, enter position. '))
            print('Folowing infomation was added\n\t\t', emails_dict[id])
        futher_proceed(emails_dict)


def edit_user_info(emails_dict: dict):
    proceed = ''
    while proceed == '':
        u_id = input('Please, enter ID you want to update. ')
        print(emails_dict[u_id])
        emails_dict[u_id].set_name(input('Enter edited name. '))
        emails_dict[u_id].set_department(input('Enter edited value for department. '))
        emails_dict[u_id].set_position(input('Enter edited value for position. '))
        print(emails_dict[u_id])
        futher_proceed(emails_dict)


def del_user_info(emails_dict: dict):
    proceed = ''
    while proceed == '':
        u_id = input('Please, enter ID you want to delete. ')
        if u_id in emails_dict:
            confirm = input(f'User {u_id} with name {emails_dict[u_id].get_name()} will be deleted.\n'
                             'If you confirm delition press "y"\n'
                             'If you want to decline operation hit "Enter"\t')
            if confirm.lower() == 'y':
                print(f'\tRecord with {emails_dict.pop(u_id)} was deleted from list')

        else:
            print("There no such name in a list")

        futher_proceed(emails_dict)




def write_file(emais_dict: dict):
    with open('emails.dat', 'wb') as output:
        pickle.dump(emais_dict, output)

def main():
    emails_dict = open_file('emails.dat')
    #print(*emails_dict.values(), sep='\n')
    us_choice = menu()

    if us_choice == 5:
        write_file(emails_dict)
        sys.exit()
    elif us_choice == 1:
        search_user_info(emails_dict)
    elif us_choice == 2:
        add_user_info(emails_dict)
    elif us_choice == 3:
        edit_user_info(emails_dict)
    elif us_choice == 4:
        del_user_info(emails_dict)
    else:
        print('This message shouldn\'t appear')


if __name__ == '__main__':
    main()