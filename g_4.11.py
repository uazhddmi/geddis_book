weight = float(input('Enter your current weight: '))
loss = 1.5

for i in range(1,7):
	weight -= loss
	print(f'After {i} month you weight\'ll be {weight}')
