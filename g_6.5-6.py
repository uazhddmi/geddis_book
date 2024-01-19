with open('number_list.txt', 'r') as f:
    summ = 0
    for line in f.readlines():
        print(line, end='')
        summ += int(line.strip())

    print('Sum is: ', summ)
