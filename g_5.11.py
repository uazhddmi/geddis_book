def main():
    num1 = int(input('Enter your 1st number: '))
    num2 = int(input('Enter your 2nd number: '))

    print(f' \t{num1}\n+\t{num2}')
    your_result = int(input("Enter you result: "))
    result = calc_sum(num1, num2)
    print(f'You right' if your_result == result else f'Almost right\nright answer is {result}')


def calc_sum(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    main()
