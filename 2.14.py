P = float(input("How much money will you add: "))
t = int(input('How many years will you hold your money: '))
in_rate = float(input('What is interest rate in %? '))/100
in_interval = int(input('How often interest is calculated: '))

final_ammount = P*((1+in_rate/in_interval)**(in_interval*t))

print(f'If you put {P}$ for {t} years with {in_rate*100}% interest rate, you will get {final_ammount:.2f}')
