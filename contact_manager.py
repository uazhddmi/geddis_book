import contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    # load existing dict with contacts
    mycontacts = load_contacts()

    choice = 0

    while choice != QUIT:
        # get user choise from menu
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # save dictionary to a file
    save_contacts(mycontacts)


def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')

        contact_dct = pickle.loads(input_file)

        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct


def get_menu_choice():
    print()
    print('Menu')
    print('-'*20)
    print('1. Find contact')
    print('2. Add contact')
    print('3. Change contact')
    print('4. Dell contact')
    print('5. Quit\n')

    choice = int(input('Please, enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Please, enter your choice: '))

    return choice


def look_up(mycontacts):
    name = input('Enter contact\'s name')

    print(mycontacts.get(name, 'Name isn\'t find'))


def add(mycontacts):
    name = input('Enter name: ')
    if name in mycontacts:
        print('This name is already in contacst')
    else:
        phone = input('Phone number: ')
        email = input('Email adress: ')

        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Contact added')


def change(mycontacts):
    name = input('Enter name: ')

    if name in mycontacts:
        phone = input('Phone number: ')
        email = input('Email adress: ')

        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Information is updated')
    else:
        print('There is no such name')


def delete(mycontacts):
    name = input('Enter name: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Record\'s deleted')
    else:
        print('There is no such name')


def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mycontacts, output_file)
    output_file.close()


if __name__ == '__main__':
    main()


