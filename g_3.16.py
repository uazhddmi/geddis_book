yr = int(input('Please, enter year '))

if yr % 100 == 0 and yr % 400 == 0:
    print('You have 29 days in February in this year')
elif yr % 100 != 0 and yr % 4 ==0:
    print('You have 29 days in February in this year')
else:
    print('You have 28 days in February in this year')
