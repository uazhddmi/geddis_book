STTAX = 0.1
LTAX = 0.05

def main():
    net_cost = float(input('Enter you net cost: '))
    st_tax = state_tax_calc(net_cost)
    l_tax = local_tax_calc(net_cost)
    print(f"Your net cost is ${net_cost:0.2f},\n\tlocal tax is ${l_tax:0.2f},\n\tstate tax is ${st_tax:.2f}.\nTotal cost is ${net_cost+st_tax+ l_tax}")

def state_tax_calc(x):
    return x*STTAX

def local_tax_calc(x):
    return x*LTAX

if __name__ == "__main__":
    main()

