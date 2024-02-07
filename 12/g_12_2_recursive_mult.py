def rec_mult(x, y):
    if y == 1:
        return x
    else:
        return x + rec_mult(x, y - 1)


print(rec_mult(3, 4))

