def rec_line(n):
    if n > 1:
        rec_line(n - 1)
    for i in range(n + 1):
        print('*'* i)
    print()


rec_line(10)