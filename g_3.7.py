clr1 = input('Please enter name of color #1 ')
clr2 = input('Please enter name of color #1 ')
if clr1 == 'red' and clr2 == 'blue'or clr1 == 'blue' and clr2 == 'red':
    print('You\'ll get violet color')
elif clr1 == 'red' and clr2=='yellow' or clr1 == 'yellow' and clr2=='red':
    print('You\'ll get orrange color')
elif clr1 == 'blue' and clr2=='yellow'or clr1 == 'yellow' and clr2=='blue':
    print('You\'ll get orrange green')
else:
    print('I can\'t define your color')
