sem = 145000*2
REV = 1.03
print(f'Payment during year 1 - {sem:.02f}')
for i in range(2,6):
	sem *= REV
	print(f'Payment during year {i} - {sem:.02f}')
