def is_prime(n):
    '''check if number is simple(True) or not(False)'''
    half = n // 2
    status = True

    for count in range(2, half + 1):
        if n % count == 0:
            status = False

    return status


def main():
    for i in range(1, 20):
        if is_prime(i + 1):
            print(i + 1, end=" ")
    print()


if __name__ == '__main__':
    main()
