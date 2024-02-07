def accerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return accerman(m - 1, 1)
    else:
        return accerman(m - 1, accerman(m, n - 1))


print(accerman(3, 2))
print(accerman(3, 0))
print(accerman(0, 2))
print(accerman(3, 1))
print(accerman(0, 5))
