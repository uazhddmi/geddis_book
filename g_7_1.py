import random
import calendar

#task 7.1 sum of sales for week 
def sales_sum(w_d:list):
    week_total = 0
    for i in w_d:
        week_total += i
    return f'Sales sum for week is {week_total}'

# def data_for_week():
    

# 7.2 
def generating_num(n:int):
    # random numbers generator
    return [random.randint(0,9) for i in range(n)] 

def printing_list(list1:list):
    # print values from list
    print('Your raffle numbers are:')
    print('-'*3, end='')
    for i in list1:
        print(i, end=' ')
    print('-'*3)

# 7.3 rainfall calculation 
def rain_data():
    # collecting data for rain for every month
    rain_data = []
    for i in range(12):
        rain_data.append(int((input(f'Enter quantity of rain for {calendar.month_name[i+1]}: ')).strip()))

    return rain_data

def calc_rain(data=[100, 200, 300, 900, 500, 100, 700, 800, 900, 700, 400, 600]):
    sum = 0 
    for i in data:
        sum += i
    max_r = max(data)
    min_r = min(data)
    max_month_list = ' and '.join(calendar.month_name[i] for i in val_index(max_r, data)) # create string of monthes with max values, separator 'and'
    min_month_list = ' and '.join(calendar.month_name[i] for i in val_index(min_r, data)) # create string of monthes with max values, separator 'and'

    
    print(f"Overall quantity of rain by year is {sum}, average quantity is {sum/12:0.2f}.")
    print(f"Maximum rain quantity was {max_r} on {max_month_list}")
    print(f"Minimum rain quantity was {min_r} on {min_month_list}")

def val_index(value, data:list):
    """find and return indexes of values in list if any or several"""
    r_list = []    
    for i in range(len(data)):
        if data[i] != value:
            pass
        else: 
            r_list.append(i+1)   
    return r_list 

# 7.4 receive 20 numbers, give back min, max, average, sum

def receive_data():
    data_list =[]
    for i in range(20):
        data_list.append(int(input(f'Enter number {i+1}: ').strip()))
    return data_list

def processing_num(data:list):
    sum = 0
    for i in data:
        sum += i
    return f'Maximum valus is {max(data)}, minimum value is {min(data)}, average is {sum/len(data):0.2f}. Sum of all numbers is {sum}'



# 7.5 reads bill numbers from file to list, asks user for bill number, check is it allowed - prompt user with message(allowed | not allowed)

def charge_accounts():
    accounts = []
    with open('charge_accounts.txt', 'r') as file:
        for i in file.readlines():
            accounts.append(int(i.strip()))

    u_account = int(input('Enter number of account: '))
    print('Account number is valid' if u_account in accounts else 'Account is not valid')

def num_is_greater(n, data:list):
    grater_than = []
    for num in data:
        if num > n:
            grater_than.append(num)
        else:
            continue  
    
    return grater_than
# task 7.5
# num = int(input('Enter your number: '))
# print(f'Following numbers are greater than {num}')
# print(*num_is_greater(num, [random.randint(0, 100) for i in range(20)]))
    
#7.6 gets 20 valid answers from file, get 20 answers from user. Compare 2 lists, answer has been passed exam | not, output quant right answers, wrong number (and which were wrong)  

def get_right_answ():
    with open('right_answers.txt', 'w') as file:
        for i in range(20):
            file.write(input(f"Right answer for question {i+1} is: ") + '\n')

# get_right_answ()

def exam():
    u_a_lst = []
    r_a_lst = []
    with open('right_answers.txt', 'r') as f1:
        for i in f1.readlines():
            r_a_lst.append(i.rstrip().upper())

    with open('student_solution.txt', 'r') as f2:
        for i in f2.readlines():
            u_a_lst.append(i.rstrip())

    r_answ = 0
    wr_answ = 0
    wr_a_pos = []
    for i in range(20):
        if u_a_lst[i] == r_a_lst[i]:
            r_answ += 1
        else:
            wr_answ += 1
            wr_a_pos.append(i+1)

    return f'{wr_answ} wrong answers. ' + f'{r_answ} right answers. ' + 'You passed exam' if r_answ > 15 else f'You failed. Your answer for questions {' '.join([str(i) for i in wr_a_pos])} was wrong'

# 7.8 check if name inserted by user is among most popular name's from file

def file_read(filename, encoding='UTF-8'):
    ''' read file by lines & return list'''
    r_list =[]
    with open(filename, 'r') as file:
        for i in file.readlines():
            r_list.append(i.rstrip())
    return r_list

def file_read_num(filename):
    ''' read file by lines & return list'''
    r_list =[]
    with open(filename, 'r') as file:
        for i in file.readlines():
            r_list.append(int(i.strip()))
    return r_list

def check_name():
    boys = file_read('BoyNames.txt')
    girls = file_read('GirlNames.txt')

    boy = input('Enter boy\'s name: ').strip()
    girl = input('Enter girl\'s name: ').strip()

    if boy != '':
        if boy in boys:
            print(f'{boy}\' is on the list')

    if girl != '':    
        if girl != '':
            if girl in girls:
                print(f'{girl} is on the list')

 # 7.9 

def us_population():
    pptn = file_read_num('USPopulation.txt')    
    in_y = int(input("Enter initial year in interval 1950-1990: ")) - 1950
    end_y = int(input("Enter clozing year in interval 1950-1990: ")) - 1950
    total = 0
    interval = pptn[in_y:end_y]
    max_in = max(interval)
    max_year = ', '.join([str(1950 + in_y + i) for i in val_index(max_in, interval)])
    min_in = min(interval)
    min_year = ', '.join([str(1950 + in_y + i) for i in val_index(min_in, interval)])
    for year in interval:
        total += year
    print('Average population {:,.02f}, maxium value was {} in {}'.format((total / (end_y - in_y)), max_in, max_year))
    print('Minimum value was {:,} in {}'.format(min_in, min_year))

#7.10 World series
def world_series(pattern):
    years_list = file_read('WorldSeriesWinners.txt')
    years_list.insert((1904-1903), '')
    years_list.insert((1994 - 1903), '')

    return f'{pattern} winned {years_list.count(pattern)} times' if pattern in years_list else f'Team {pattern} have never won'

# 7.11 Lo Shu square. 


def gen_matrix_num9(raw, col): # generates r,c matrix with random numbers to 9 
    matrix = [[0]*raw for i in range(col)]
    for i in range(raw):
        for j in range(col):
            matrix[i][j] = random.randint(0,9)
    return matrix


def gen_matrix(raw, col):
    return [[0]*raw for i in range(col)]

def lo_shu(matrix):
    s_row1 = s_row2 = s_row3 = s_s1 = s_s2 = s_s3 = sd1 = sd2 = 0
    num = len(matrix)
    for i in range(num):
            s_row1 += matrix[i][0]
            s_row2 += matrix[i][1]
            s_row3 += matrix[i][2]
            s_s1 += matrix[0][i]
            s_s2 += matrix[1][i]
            s_s3 += matrix[2][i]
        
    sd1 = matrix[0][0] + matrix[1][1] + matrix[2][2] 
    sd2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
    print(s_row1 , s_row2 , s_row3 , s_s1 , s_s2 , s_s3 , sd1 , sd2)
    return 'Lo Chu' if s_row1 == s_row2 == s_row3 == s_s1 == s_s2 == s_s3 == sd1 == sd2 == 15 else 'not Lo Chu'

#7.12 define all prime numbers in range till user defined numbers

def prime_number(num:int):
    flag = True 
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
        else:
            flag = True
    return f'{num} is a prime number' if flag else f'{num} is not prime'

def g_7_12(): 
    '''shows prime numbers in user selected range'''
    user_num = int(input("Your number is: "))

    numbers = [number for number in range(2, user_num +1)]

    for i in range(len(numbers)):
        print(prime_number(numbers[i]))

# 7.13 ball with 

def magic_ball():
    answers = file_read('8_ball_responses_en.txt')    
    while True:
        input("Enter you question: ")
        print(f'You answer is {answers[random.randint(0, len(answers))]}')
        check = input('Do you want to play more? if no press No/n: ')
        if 'n' in check.lower():
            break
        else:
            continue

# magic_ball()m


# g_7_12()
    

# print(lo_shu(gen_matrix_num9(3,3)))
    

# print(world_series('Oakland Athletics'))
# print(world_series('Dinamo Kiev'))
# us_population()
# check_name()


# print(exam())

# charge_accounts()
# calc_rain()

# print(sales_sum(data_for_week()))

# printing_list(generating_num(7))
# print(processing_num(receive_data()))

