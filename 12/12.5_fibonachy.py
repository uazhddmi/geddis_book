def fibonachy(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonachy(n - 1) + fibonachy(n - 2)

for i in range(1,11):
    print(fibonachy(i))


