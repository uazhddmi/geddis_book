from g_5_17 import is_prime


def main():
    count_pr = 0
    for i in range(101):
        res = is_prime(i)
        print(f'{i}', 'is prime' if res else 'in\'t prime')
        if res:
            count_pr += 1
    print('*'*40)
    print(f'Prime numbers {count_pr},\n\tnot prime {100 - count_pr}')


if __name__ == '__main__':
    main()
