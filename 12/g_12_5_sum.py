import time


def sum_list(data: list):
    n = len(data)
    if n == 1:
        return data[0]
    else:
        return data[n - 1] + sum_list(data[:n - 1])


list1 = [i**2 for i in range(100)]
print(sum_list([1, 2, 3, 4, 5]))
# print(sum_list([]))
start = time.time()
print(sum_list(list1))
end = time.time()
print('Sum recur', end - start)

def sum_fanc(data: list):
    d_sum = 0
    for i in data:
        d_sum += i
    return d_sum

start = time.time()
print(sum_fanc(list1))
end = time.time()
print('Sum for', end - start)






