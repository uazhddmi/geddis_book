RATIO = 0.6214
def main():
    '''asks for distance in km & convert it to miles
    '''
    klms = float(input('Enter distance in km: '))

    miles = km2miles(klms)

    print(f'{klms} kilometers are {miles:.2f} in miles')

def km2miles(x):
    return x*RATIO

if __name__ =='__main__':
    main()
