RET = 0.8

def main():
    morgage = float(input('You cost is: '))

    print(f'You minimal insuranse should be ${calc_ins_rate(morgage):0.2f}')

def calc_ins_rate(vol):
    return RET*vol

main()


