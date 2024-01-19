TAX = 18
MIL_TAX = 1.5


def interest_calc(vol, irate: float, mth: int):
    return vol * (1 + irate / 100 / 12) ** mth


def calc_tax(n):
    return n * ((TAX + MIL_TAX) / 100)


def main():
    vol = float(input("Please, enter your money amount: "))
    irate = float(input("Please, enter interest rate: "))
    mth = int(input("Please, enter how much months should be taken in account: "))
    profit = interest_calc(vol, irate, mth)
    tax = calc_tax(profit - vol)
    print(f"In {mth} months you will have ${profit - tax:.2f} at your account")
    print(f'Your profit will be {profit - tax -vol:.2f}')


if __name__ == '__main__':
    main()
