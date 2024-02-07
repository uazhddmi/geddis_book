def pow_rec(m, n):
    if n == 1:
        return m
    else:
        return m * pow_rec(m, n - 1)


print(pow_rec(2,3))
print(pow_rec(2,5))
