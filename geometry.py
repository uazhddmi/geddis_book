import circle, rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    #choice command with cycle and contain user choice
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        #user input
        choice = int(input('Make your choice'))

        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Enter radius'))
            print('Area is', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Enter radius'))
            print('Circumvent is', circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Width of rectangle: '))
            length = float(input('Length of rectangle: '))
            print('Square is: ', rectangle.area(width,length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Width of rectangle: '))
            length = float(input('Length of rectangular: '))
            print('Perimeter is: ', rectangle.perimeter(width,length))
        elif choice == QUIT_CHOICE:
            print('Exit programm...')
        else:
            print('Mistake, no such choice.')

    #show menu
def display_menu():
    print('\tMenu')
    print('1. Circle square')
    print('2. Circle circumference')
    print('3. Rectangular square')
    print('4. Rectangular square')
    print('5. Exit')

main()
