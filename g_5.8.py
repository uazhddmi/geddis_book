PAINT = 5
WORK = 8
WORK_RATE = 2000


def main():
    area = float(input('Enter area '))
    paint_price = float(input('Enter paint cost per 1 tank 5l: '))

    paint_cost = calc_paint_cost(area, paint_price)
    paint_quantity = calc_paint_quantity(area)
    wk_hours = calc_wk_hours(area)
    wk_cost = calc_wk_cost(area)

    print(f'To paint {area} m2 area you will need:')
    print(f'\t\t{int(paint_quantity)} tanks of paint')
    print(f'\t\t{wk_hours:.2f} hours of work')
    print(f'Paint cost will be ${paint_cost:.2f}')
    print(f'Work cost will be ${wk_cost:.2f}')
    print('-'*40)
    print(f'Total cost will be ${wk_cost + paint_cost:.2f}')


def calc_paint_cost(area, paint_price):
    return calc_paint_quantity(area) * paint_price


def calc_paint_quantity(area):
    return area / 10


def calc_wk_hours(area):
    return area * WORK / 10


def calc_wk_cost(area):
    return calc_wk_hours(area) * WORK_RATE


if __name__ == '__main__':
    main()
