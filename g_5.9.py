FED_TAX = 0.025
STATE_TAX = 0.05


def main():
    sales = int(input("Enter month's sale: "))

    print(f'Federal tax for you month sale is ${calc_fed_tax(sales):.2f}')
    print(f'State tax for you month sale is ${calc_state_tax(sales):.2f}')
    print(f'Total taxes are ${calc_fed_tax(sales) + calc_state_tax(sales):.2f}')


def calc_fed_tax(sales):
    return sales * FED_TAX


def calc_state_tax(sales):
    return sales * STATE_TAX


if __name__ == '__main__':
    main()
