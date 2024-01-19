num = int(input('Please enter your number: '))

if num == 0:
    print(f'You number is {num}, your pocket color is green')
elif 1 <= num <=10:
    if num % 2 == 0:
        print(f'You number is {num}, your pocket color is red')
    else:
        print(f'You number is {num}, your pocket color is black')
elif 11 <= num <= 18:
    if num % 2 == 0:
        print(f'You number is {num}, your pocket color is red')
    else:
        print(f'You number is {num}, your pocket color is black')
elif 19 <= num <= 28:
    if num % 2 != 0:
        print(f'You number is {num}, your pocket color is red')
    else:
        print(f'You number is {num}, your pocket color is black')
elif 29 <= num <= 36:
    if num % 2 == 0:
        print(f'You number is {num}, your pocket color is red')
    else:
        print(f'You number is {num}, your pocket color is black')
else:
    print('You entered wrong number, should be from 0 to 36')
