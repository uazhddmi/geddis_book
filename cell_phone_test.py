# tests class CellPhone

import cellphone


def main():
    man = input('Enter manufacture: ')
    mod = input('Enter model: ')
    retail = float(input('Enter retail price: '))

    phone = cellphone.CellPhone(man, mod, retail)

    print('Here is your data')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model: {phone.get_model()}')
    print(f'Retail price: {phone.get_retail_price()}')


if __name__ == "__main__":
    main()


