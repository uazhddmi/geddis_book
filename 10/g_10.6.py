import datetime
class Patient:
    def __init__(self, name, middlename, surname, address, city, reg, zipcode):
        self.__name = name
        self.__middlename = middlename
        self.__surname = surname
        self.__address = address
        self.__city = city
        self.__reg = reg
        self.__zipcode

    def set_name(self, name):
        self.__name = name

    def set_middlename(self, middlename):
        self.__middlename = middlename

    def set_surname(self, surname):
        self.__surname = surname

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_reg(self, reg):
        self.__reg = reg

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode


    def get_name(self):
        return self.__name

    def get_middlename(self):
        return self.__middlename

    def get_surname(self):
        return self.__surname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_zipcode(self):
        return self.__zipcode


class Procedure:
    def __init__(self, procedure, procedure_date, doctor_name, cost):
        self.__procedure = procedure
        self.__procedure_date = procedure_date
        self.__doctor_name = doctor_name
        self.__cost = cost

    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    def set_cost(self, cost):
        self.__cost = cost

    def get_procedure(self):
        return self.__procedure

    def get_procedure_date(self):
        return self.__procedure_date

    def get_doctor_name(self):
        return self.__doctor_name

    def get_cost(self):
        return self.__cost




procedure1 = Procedure('doctor visit', datetime.date.today() , 'Irvin', 250 )
print(procedure1.get_procedure_date(), procedure1.get_procedure(), procedure1.get_cost(), procedure1.get_doctor_name())
procedure1.set_doctor_name('Elvis')
print(procedure1.get_procedure_date(), procedure1.get_procedure(), procedure1.get_cost(), procedure1.get_doctor_name())
