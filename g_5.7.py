A = 20
B = 15
C = 10

def cost_calculation(a, b, c):
    return a * A + b * B + c * C

def main():
    a = int(input('How many A-class tickets were sold '))
    b = int(input('How many B-class tickets were sold '))
    c = int(input('How many C-class tickets were sold '))

    print(f'You receive ${cost_calculation(a, b , c):.02f}')

if __name__== '__main__':
    main()