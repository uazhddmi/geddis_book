def main():
    grade1 = int(input('Your 1st grade is: '))
    print('\t\t',determine_grade(grade1))
    grade2 = int(input('Your 2nd grade is: '))
    print(determine_grade(grade2))
    grade3 = int(input('Your 3rd grade is: '))
    print(determine_grade(grade3))
    grade4 = int(input('Your 4th grade is: '))
    print(determine_grade(grade4))
    grade5 = int(input('Your 5th grade is: '))
    print(determine_grade(grade5))
    average = calc_average(grade1, grade2, grade3, grade4, grade5)
    print('#'*30)
    print('Average grade is', determine_grade(average))

def calc_average(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 +n5)/5


def determine_grade(gr):
    if gr < 60:
        return 'F'
    elif 60 <= gr < 70:
        return 'D'
    elif 70 <= gr < 80:
        return 'C'
    elif 80 <= gr < 90:
        return 'B'
    else:
        return 'A'


if __name__ == '__main__':
    main()
