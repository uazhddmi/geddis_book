#constant ratio
INCHES_PER_FOOT = 12
# convert feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT


def main():
    feet = float(input('Enter you feet quantity: ').strip())
    print(f'{feet} equal to {feet_to_inches(feet):.2f} inches')


if __name__ == '__main__':
    main()
