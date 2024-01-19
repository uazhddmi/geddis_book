#contant g m/s2
G = 9.8


def main():
    t = 1 
    while t < 11:
        print(f'in {t} second body will pass {calc_distance(t):.2f} m')
        t += 1

def calc_distance(t):
    return G*t**2/2


if __name__ == '__main__':
    main()

