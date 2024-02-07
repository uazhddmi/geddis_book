class RetailItem:
    def __init__(self, description, quantity, price):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def __str__(self):
        return f'{self.__description} in quantity of {self.__quantity} pcs is available for ${self.__price}'

def main():
    item1 = RetailItem('Пиджак', 12, 59.95)
    item2 = RetailItem('Дизайнерские джинсы', 40, 34.95)
    item3 = RetailItem('Рубашка', 20, 24.95)

    print(item1)
    print(item2)
    print(item3)


if __name__=='__main__':
    main()