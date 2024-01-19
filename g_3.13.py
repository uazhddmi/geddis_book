wght = float(input("Your package weight is in gramms "))

if wght < 200:
    print('Delivery cost is 150$')
elif 200 <= wght < 600:
    print('Delivery cost is 300$')
elif 600 <= wght < 1000:
    print('Delivery cost is 400$')
else:
    print('Delivery cost is 475$')

