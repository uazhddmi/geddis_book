Fc = 9
Yc = 4


def main():
    fg = int(input('Enter fat in grams: '))
    fcal = calc_F_clr(fg)
    yg = int(input('Enter yglevody in grams: '))
    ycal = calc_Y_clr(yg)
    print('You take', f'{fcal:.0f} calories from fat' if fcal > ycal else f'{ycal:.0f} calories from yglevody')


def calc_F_clr(g):
    return Fc * g


def calc_Y_clr(g):
    return Yc * g


if __name__ == '__main__':
    main()
