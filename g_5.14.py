def kinetic_energy(m, v):
    return (m * v ** 2) / 2


def main():
    m = int(input("Enter your mass (kg): "))
    v = int(input('Enter your speed (m/s)'))

    print(kinetic_energy(m, v))


if __name__ == '__main__':
    main()
