def is_prime(n):
    '''check if number is simple(True) or not(False)'''
    half = n // 2
    status = True

    for count in range(2, half + 1):
        if n % count == 0:
            status = False

    return status


def main():
    num = int(input('Enter your number: '))
    res = is_prime(num)
    print(f'{num}', 'is simple' if res == True else 'in\'t simple')


if __name__ == '__main__':
    main()
