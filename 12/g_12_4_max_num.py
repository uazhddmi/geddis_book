def find_max_num(data: list):
    n = len(data)
    if n == 0:  # In case when empty list is given
        return None
    elif n == 1:
        return data[0]
    else:
        temp = find_max_num(data[0:n-1])
        if data[n-1] > temp:
            return data[n-1]
        else:
            return temp


print(find_max_num([1, 2, 4, 5, 6]))
print(find_max_num([]))
