K = 0.6 # coefficient for cost estimatin out of 1
TAX = 0.72 # tax in cent
def main():
    overall_cost = float(input('Cost of your house is: $'))
    est_cost = calc_est_cost(overall_cost)
    print(f'Estimated cost of you house is ${est_cost:.2f}')
    tax = tax_calc(est_cost)
    print(f'Your tax for your house is %{tax:.2f}')

def calc_est_cost(cost):
    return cost*K

def tax_calc(est_cost):
    return est_cost*TAX/100

if __name__=='__main__':
    main()
