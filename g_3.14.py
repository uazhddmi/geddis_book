mass = float(input('Please enter your weight in kg '))
ht = float(input('Please enter your height in m (example: 1.81) '))
imt = mass / ht**2
if imt < 18.5:
    stat = 'less than normal'
elif 18.5 <= imt < 25:
    stat = 'optimal'
else:
    stat = 'over'
print(f'You imt is {imt:.1f}. You have {stat} weight')
