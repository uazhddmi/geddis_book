R = float(input('Length of the yard in m: '))
E = float(input('Distance for holders in m: '))
S = float(input('Distance between grapes in m: '))

print(f'There are {(R-2*E)//S:.0f} will fitt at the lane')
