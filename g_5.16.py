import random


def count_even_odd(n):
    even = 0
    odd = 0
    x = 0
    while x < n:
        y = random.randint(0, int(n))
        if y % 2 == 0:
            even += 1
        else:
            odd += 1
        x += 1
    return even, odd


def main():
    n = int(input('Please, enter your number (n): '))
    print(f'Program counts how many odd and even numbers ate at {n} numbers generated randomly')
    even, odd = count_even_odd(n)
    print(f'There were {even} & {odd} numbers')


if __name__ == '__main__':
    main()
