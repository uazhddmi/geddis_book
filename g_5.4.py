def main():
    '''ask for month's cost of petrol, credit payment, insurance, oil, tires\
            service
    '''
    petrol= float(input('Petrol cost: '))
    credit_payment= float(input('Petrol cost: '))
    insurance= float(input('Petrol cost: '))
    oil= float(input('Petrol cost: '))
    tires= float(input('Petrol cost: '))
    service= float(input('Petrol cost: '))

    month_cost = calc_month_cost(petrol, credit_payment, insurance, oil, tires,service)
    print(f'You spend ${month_cost:.2f} a month for your car')
    print(f'You spend ${calc_year_cost(month_cost):.2f} a year') 

def calc_month_cost(petrol, credit_payment, insurance, oil, tires,service):
    return petrol + credit_payment + insurance + oil + tires + service

def calc_year_cost(x):
    return 12*x

if __name__=='__main__':
    main()
