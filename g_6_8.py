import sys 

count = 0
sum = 0
try:
    with open('random_numbers.txt', 'r') as file:
        for line in file.readlines():
            if bool(line):
                sum += int(line.rstrip())
                count += 1
except IOError:
    sys.exit("file is already open")
except ValueError:
    sys.exit('value can\'t be converted to a number')
try:    
    print(f'There are {count} in file')
    print(f'Average number is {sum / count}')
except ZeroDivisionError:
    print('no numbers, so can\'t count average(division by zero)')