def area(width, length):
    return width * length

def perimeter(width, length):
    return 2 * (width + length)

def main():
    width = float(input('Enter rectangular width: '))
    length = float(input('Enter rectangular length'))
    print('Rectangular square is: ', area(width, length))
    print('Perimeter is: ', perimeter(width, length))

if __name__ == '__main__':
    main()
