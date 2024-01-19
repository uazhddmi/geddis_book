ST = 0.05
LT = 0.025
cost = float(input('Enter cost of your goods: '))
c_ST = cost*ST 
c_LT = cost*LT
print(f'State tax for your {c_ST:.2f} goods')
print(f'Local tax for you {c_LT:.2f} goods')
print(f'Total of taxes is {c_ST+c_LT:.2f}')
print(f'You total with taxes is {cost+c_ST+c_LT:.2f}')
