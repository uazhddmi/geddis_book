c5c = int(input('How many 5c coins will you put? :'))
c10c = int(input('How many 10c coins will you put? :'))
c50c = int(input('How many 50c coins will you put? :'))

sum = c5c*5 +c10c*10+c50c*50

if sum == 100:
    print('You win, you put 1 ruble straigh')
elif sum < 100:
    print('You give less than 1 ruble')
else:
    print('You give more than 1 ruble')
