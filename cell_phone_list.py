import cellphone

def main():
    phones = make_list()

    print('There are your data')
    display_list(phones)


def make_list() -> list:
    phone_list = []

    print('Enter data for 5 phones.')
    for count in range(1, 6):
        print(f'Cellphone number {count}: ')
        man = input('Enter manufacture: ')
        mod = input('Enter model: ')
        retail = float(input('Enter retail price: '))
        print()
        phone = cellphone.CellPhone(man, mod, retail)

        phone_list.append(phone)

    return phone_list


def display_list(phones_list:list):
    for phone in phones:
        print(f'Cellphone manufacture: {phone.get_manufact()}')
        print(f'Cellphone model: {phone.get_model()}')
        print(f'Cellphone price: {phone.get_retail_price()}', '\n')



if __name__=="__main__":
    main()





