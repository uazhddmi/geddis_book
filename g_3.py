#1
try:
    num = int(input('number of weekday: '))
except ValueError:
    exit('is not a number')

if num == 1:
    print('WeekDay is Monday')
elif num == 3:
    print('WeekDay is Wednesday')
elif num == 2:
    print('WeekDay is Tuesday')
elif num == 4:
    print('WeekDay is Thuesday')
elif num == 5:
    print('WeekDay is Friday')
elif num == 6:
    print('WeekDay is Saturday')
elif num == 7:
    print('WeekDay is Sunday')
else:
    print('wrong number')

#2
rect1 = input('1st rectangular width x height')
w, h = rect1.strip().split('x')
w = int(w.strip())
h = int(h.strip())
rect2 = input('1st rectangular width x height')
w2, h2 = rect2.strip().split('x')
w2 = int(w2.strip())
h2 = int(h2.strip())
if w*h < w2*h2:
    print('1st rectangular is smaller')
elif w*h > w2*h2:
    print('2nd rectangular is smaller')
else:
    print('rectangulars are equal')

#3
num = int(input('enter arabic number in range between 1 to 10 :'))

if num == 1:
    print(f'Roman number for arabic {num} is I')
elif num == 2:
    print(f'Roman number for arabic {num} is II')
elif num == 3:
    print(f'Roman number for arabic {num} is III')
elif num == 4:
    print(f'Roman number for arabic {num} is IV')
elif num == 5:
    print(f'Roman number for arabic {num} is V')
elif num == 6:
    print(f'Roman number for arabic {num} is VI')
elif num == 7:
    print(f'Roman number for arabic {num} is VII')
elif num == 8:
    print(f'Roman number for arabic {num} is VIII')
elif num == 9:
    print(f'Roman number for arabic {num} is IX')
elif num == 10:
    print(f'Roman number for arabic {num} is X')


#5

mass = int(input('Please, enter you mass :'))
wght = mass*9.8
if wght > 500:
    print('body is too heavy')
elif wght < 100:
    print('body is too light')
else:
    print(f'your weight then {wght:.2f} Nm')

#6
date = int(input('pls enter your date :'))
month = int(input('pls enter your month '))
year = int(input('pls enter your year '))
if date*month == year:
    print('the date is magic')
else:
    print('the date isn\'t magic')
