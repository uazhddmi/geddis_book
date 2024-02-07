from g_10_5 import RetailItem as Ri


class CashRegister:
    def __init__(self):
        self.__basket = []

    def clear(self):
        self.__basket = []

    def purchase_item(self, retail):
        self.__basket.append(retail)
        print(f'Item {retail} was added to a basket')

    def get_total(self):
        total = 0

        for item in self.__basket:
            total += item.get_price()

        return total

    def show_item(self):
        print('Goods you already put in a basket')
        for item in self.__basket:
            print(item.get_description())


item1 = Ri('Пиджак', 12, 59.95)
item2 = Ri('Дизайнерские джинсы', 40, 34.95)
item3 = Ri('Рубашка', 20, 24.95)


to_buy = CashRegister()

to_buy.purchase_item(item1)
to_buy.purchase_item(item2)
to_buy.purchase_item(item3)


to_buy.show_item()

print(f'Total cost is ${to_buy.get_total():.02f}')

to_buy.clear()
to_buy.show_item()
