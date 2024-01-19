days = int(input('Enter days quantity: '))
print('-'*40)
sal = 1
total = 0.01
print(f'Salary for day 1 is {sal/100} rubles')
for i in range(2, days+1):
	sal *=2
	total += sal/100
	print(f'Salary for day {i} is {sal/100} rubles')

print('-'*40)
print(f'Total salary is {total:.02f} rubles')
