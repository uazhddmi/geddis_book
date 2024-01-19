def main():
    num1 = int(input('Enter your 1st number: '))
    num2 = int(input('Enter your 2nd number: '))
    print('*'*30)
    print(calc_max(num1, num2), 'is greater')


def calc_max(num1, num2):
    return num1 if num1 > num2 else num2


if __name__ == '__main__':
    main()
