distance = float(input("Enter distance you've passed "))
fuel_cons = float(input("Enter your car fuel consumption "))

fc = distance/fuel_cons
print(f'You car wasted {fc:.2f} km per l')
