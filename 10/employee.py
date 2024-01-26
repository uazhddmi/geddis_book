class Employee:
    def __init__(self, id, name='', department='', position=''):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__position = position

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_position(self, position):
        self.__position = position

    def get_id(self):
        return  self.__id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position


    def __str__(self):
        return (f'Employee id - {self.__id}, name - {self.__name}, department - {self.__department}, '
                f'position - {self.__position}')


