# #7.6
# text = file_read('text.txt')

# total = 0
# for line in text:
#     total += len(line.split())
# print(f'Average number of words per sentence is {total/len(text)}')

# #8.7

# print('8.7')
# up_let = low_let = num_qt = white_qt = 0
# filename = 'text.txt'
# with open(filename, 'r') as file:
#         for i in file.readlines():
#               for symb in i:
#                     if symb.isdigit():
#                           num_qt += 1
#                     elif symb.isupper():
#                           up_let += 1
#                     elif symb.islower():
#                           low_let += 1
#                     elif symb.isspace():
#                           white_qt += 1

# print(f'upper letter: {up_let}, low letters: {low_let}, numbers: {num_qt}, white symbols: {white_qt}')

# 8.8
def correct_capita(line: str):
    # capitalize first letter in sentence and return string
    punct = ('.', '?', '!')
    new_sentence = True
    words = line.split()
    new_words = []
    for word in words:
        if new_sentence:
            new_words.append(word.capitalize())
        else:
            new_words.append(word)
        if word[-1] in punct:
            new_sentence = True
        else:
            new_sentence = False
    return ' '.join(new_words)


def correct_capita1(line: str):
    # capitalize first letter in sentence and return string
    punct = ('.', '?', '!')
    new_sentence = True
    result = ''
    for word in line.split():
        if new_sentence:
            result += word.capitalize() + ' '
        else:
            result += word + ' '
        if word[-1] in punct:
            new_sentence = True
        else:
            new_sentence = False
    return result


# print(correct_capita('simble line. of Text that? contain this!'))
# print(correct_capita1('simble line. of Text that? contain this!'))


# 8.10

def quant_symbols(line="any siple line of code thata has several words"):
    temp_d = []
    for symbol in line:
        temp_d.append(symbol)
    m_t = 0
    for i in temp_d:
        qt = temp_d.count(i)
        if qt > m_t:
            m_t = qt
            s_s = i
        else:
            continue

    return f'symbol "{s_s}" appeared {m_t} times(max)'


def quant_symbols1(line="any siple line of code thata has several words"):
    ''''using tuple to remove duplicat and speed up process'''
    temp_d = []
    for symbol in line:
        temp_d.append(symbol)
    m_t = 0
    temp_d = tuple(temp_d)
    for i in temp_d:
        qt = temp_d.count(i)
        if qt > m_t:
            m_t = qt
            s_s = i
        else:
            continue

    return f'symbol "{s_s}" appeared {m_t} times(max)'


# #compare time execution with dict and tuple
# st = time.time()
# print(quant_symbols())
# end = time.time()
# print(end - st)
# st = time.time()
# print(quant_symbols1())
# end = time.time()
# print(end - st)

def word_devisor(line='AnyLineWIthout_witeSpaces'):
    result = line[0]
    for i in line[1:]:
        if i.isupper():
            result += " " + i.lower()
        else:
            result += i
    return result


# print(word_devisor())

# 8.12

def zhargon(line="i slept all night long"):
    result = []
    _ = line.split()
    for i in _:
        if len(i) == 1:
            result.append(i + 'AH')
        else:
            result.append(i[1:] + i[0] + 'AH')

    return ' '.join(result)


# print(zhargon())

# 8.13

def power_ball():
    with open('pbnumbers.txt', 'r') as file:
        l_nums = [] # all numbers
        pb_nums = []  # pb numbers
        c_nums = []   # common numbers without pb
        for i in file.readlines():
            temp_list = i.rstrip().split()
            for j in temp_list:
                l_nums.append(j)
            pb_nums.append(temp_list[-1])
            for x in temp_list[:-1]:
                c_nums.append(int(x))



    return l_nums, pb_nums, c_nums


def n_greatest_num(num, numbers: tuple):
    d = {}
    lst, pb_nums, c_nums = numbers[0], numbers[1], numbers[2]

    for i in lst:
        d[i] = d.get(i, 0) + 1

    line = []
    for key, value in d.items():
        line.append((value, key))

    print(f'{num} less appeared numbers')

    line.sort()
    for key, value in line[0:num]:
        print(f'\t\tNumber {value} appeared {key} times')

    line.sort(reverse=True)
    print(f'{num} most appeared numbers')

    for key, value in line[0:num]:
        print(f'\t\tNumber {value} appeared {key} times')

    print('Numbers from 1 to 69')
    for i in range(1, 70):
        print(f'\t\t\t{i} appeared {c_nums.count(i)} times')

    print('Power ball\'s numbers from 1 to 26')
    for i in range(1, 27):
        if i < 10:
            i = '0' + str(i)

        print(f'\t\t\t{i} appeared {pb_nums.count(str(i))} times')

n_greatest_num(10, power_ball())
# print(type(power_ball()))

#8.14

# average price for file 1993 to 2013
# average price for month
# max and min per year and its date for every year
# prices sorted descending & ascending

def read_file():
    with open('GasPrices.txt', 'r') as file:
        input_file = file.read()

    return input_file

# print(read_file())
input_file = read_file()
for i in input_file:
    i.rstrip()
    date, price = input_file.split(':')

total = 0
for i in price:
    total += int(i)

print(f'Average price is {total/len(input_file)}')

