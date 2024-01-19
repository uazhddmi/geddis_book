num = int(input('Your number is: '))
fact = 1 
for i in range(1, num+1):
	fact *= i 

print(f'{num}! is {fact}')
