# BASE_YEAR = 1903

def create_dictionary(file):
    dict1 = {}
    for line in file:
        dict1[line] = dict1.get(line, 0) + 1
    return dict1


def winners(file: list):
    years_winner = {}

    for i in range(len(file)):
        # year = BASE_YEAR +i
        # if year > 1903:
        #     year += 1
        # if year > 1994:
        #     year += 1
        years_winner[(i + 1903)] = file[i]

    return years_winner


def read_file(file: str):
    with open(file, 'r') as f:
        result = [i.rstrip() for i in f.readlines()]
    return result


def main():
    initial_data = read_file('WorldSeriesWinners.txt')

    result_dict = create_dictionary(initial_data)

    text = 'No WorldSeries this year'
    # insert 2 sceeped years in list of winners
    initial_data.insert((1904 - 1903), text)
    initial_data.insert((1994 - 1903), text)
    winner_of_year = winners(initial_data)

    us_year = 0
    while 2009 > us_year < 1903:
        us_year = int(input("Enter year in range 1903-2009: "))
    if us_year == 1904 or us_year == 1994:
        print(text)
    else:
        winner = winner_of_year[us_year]
        times = result_dict[winner]
        print(f'In {us_year} the winner was {winner}')
        print(f'From 1903 to 2009 they were winners {times} time\
              {'s' if times > 1 else ''}')


if __name__ == '__main__':
    main()
