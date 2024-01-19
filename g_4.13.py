s_qt = int(input('Starting quantity: '))
in_rt = int(input('Increase rate (in %): '))
days = int(input('Days: '))
print("Days\t\tQuantity")
print(f"1\t\t{s_qt}")
for i in range (2, days+1):
	s_qt *= (1 + in_rt/100)
	print(f"{i}\t\t{s_qt:.02f}")
