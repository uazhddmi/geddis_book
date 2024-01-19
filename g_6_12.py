january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31 
november = 30 
december = 31

def count_st(file, month_name, days):
    sum = 0 
    for i in range(days):
        sum += int(file.readline())
    average = sum / days

    print(f'Среднее количество шагов в {month_name} составило {average:0.1f}')

def main():
    file = open('steps.txt', 'r')

    count_st(file,'январе', january)
    count_st(file,'феврале', february)
    count_st(file,'марте', march)
    count_st(file,'апреле', april)
    count_st(file,'мае', may)
    count_st(file,'июне', june)
    count_st(file,'июле', july)
    count_st(file,'августе', august)
    count_st(file,'сентябре', september)
    count_st(file,'октябре', october)
    count_st(file,'ноябре', november)
    count_st(file,'декабре', december)

    file.close()


main()
