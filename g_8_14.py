# count average price per year for every year in range 1993 - 2013 +
# count average price per month in file +
# find max & min price per year and show it's date +
# show list with increasing price order
# show list with decreasing price order
import re

BEGIN = 1993
END = 2013


#
def search_value(line: str, year: int):
    regex = r'(\d{2})-(\d{2})-(\d{4}):(\d\.\d+)'
    total = 0
    count = 0
    for i in line:
        res = re.search(regex, i.rstrip())
        if res.group(3) == str(year):
            total += float(res.group(4))
            count += 1
    return f'{total / count:0.2f}'


f_h = open('GasPrices.txt', 'r')
file = f_h.readlines()


# for y in range(BEGIN, END + 1):
#     print(f'Average price in {y} year was {search_value(file, y)}')

def search_av_per_month(line, year, month):
    regex = r'(\d{2})-(\d{2})-(\d{4}):(\d\.\d+)'
    total = 0
    count = 0
    for i in line:
        res = re.search(regex, i.rstrip())
        if res.group(3) == str(year):
            if int(res.group(1)) == month:
                total += float(res.group(4))
                count += 1

    return f'{total / count:0.2f}' if count != 0 else '0, no Data'


# for yr in range(BEGIN, END + 1):
#     for y in range(1, 13):
#         print(f'Average price in {y} month of the {yr} year was {search_av_per_month(file, yr, y)}')


def search_max_min_per_year(line, year):
    regex = r'(\d{2})-(\d{2})-(\d{4}):(\d\.\d+)'
    maxv = 0
    max_day = ''
    minv = 10
    min_day = ''
    for i in line:
        res = re.search(regex, i.rstrip())
        if res.group(3) == str(year):
            val = float(res.group(4))
            if val > maxv:
                maxv = val
                max_day = res.group(1) + '-' + res.group(2)
            if val < minv:
                minv = val
                min_day = res.group(1) + '-' + res.group(2)
    return maxv, max_day, minv, min_day


for yr in range(BEGIN, END + 1):
    maxv, max_day, minv, min_day = search_max_min_per_year(file, yr)
    print(f'At {yr} year there was max {maxv} price on {max_day}, and min {minv} price on {min_day}')
