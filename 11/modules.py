class Employee:
    def __init__(self, name, uid):
        self.__name = name
        self.__uid = uid

    def set_name(self, name):
        self.__name = name

    def set_uid(self, uid):
        self.__uid = uid

    def get_name(self):
        return self.__name

    def get_uid(self):
        return self.__uid


class ProductionWorker(Employee):
    def __init__(self, name, uid, shift_num, h_rate):
        Employee.__init__(self, name, uid)
        self.__shift_num = shift_num
        self.__h_rate = h_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_h_rate(self, h_rate):
        self.__h_rate = h_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_h_rate(self):
        return self.__h_rate


class ShiftSupervisor(Employee):
    def __init__(self, name, uid, paid, bonus):
        super().__init__(name, uid)
        self.__paid = paid
        self.__bonus = bonus

    def set_paid(self, paid):
        self.__paid = paid

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_paid(self):
        return self.__paid

    def get_bonus(self):
        return self.__bonus


user3 = ShiftSupervisor('Al', 12, 1000, 100)
# print('Production worker')
# user1 = ProductionWorker(input('Name'), input('ID'), input('Shift num'), input('rate'))
# print('Employee')
# user2 = Employee(input('Name'), input('ID'))
# print('Production manager')
# user3 = ShiftSupervisor(input('Name'), input('ID'), input('Paid'), input('bonus'))


# print(user1.get_name(), user1.get_uid(), user1.get_shift_num(), user1.get_h_rate())
# print(user3.get_name(), user3.get_uid(), user3.get_paid(), user3.get_bonus())
# print(user2.get_name(), user2.get_uid())


assert user3.get_bonus() == 100


class Person:
    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num


class Customer(Person):
    def __init__(self, name, address, phone_num, c_id, mail_list: bool):
        super().__init__(name, address, phone_num)
        self.__c_id = c_id
        self.__mail_list = mail_list

    def get_c_id(self):
        return self.__c_id

    def get_mail_list(self):
        return self.__mail_list
