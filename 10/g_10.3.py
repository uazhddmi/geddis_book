class Information:
    def __init__(self, name, address, age, number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address

    def set_age(self, age):
        self.__age

    def set_age(self, number):
        self.__number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_number(self):
        return self.__number


user1 = Information('Zhora', 'Dnipro', 36, '0504801832')
print(user1.get_name())
user1.set_name("Vika")

print(user1.get_name())