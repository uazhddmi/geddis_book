import vehicles


def main():
    user_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)


    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('Used cars at stock')
    print('='*20)
    print('There is such car:')
    print('Made by:', user_car.get_make())
    print('Model:', user_car.get_model())
    print('Mileage:', user_car.get_mileage())
    print('Price:', user_car.get_price())
    print('Quantity of doors:', user_car.get_doors())

    print('There is such track:')
    print('Made by:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())

    print('There is such SUV:')
    print('Made by:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Quantity of doors:', suv.get_pass_cap())


if __name__ == '__main__':
    main()
