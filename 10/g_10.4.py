class Employee:
    def __init__(self, name, inn, dep, pos):  # dep - department, pos - position
        self.__name = name
        self.__inn = inn
        self.__dep = dep
        self.__pos = pos

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return (f'Employee name is {self.__name},\n'
                f'INN is {self.__inn},\n'
                f'works at {self.__dep},\n'
                f'position is {self.__pos}')


Employee1 = Employee()
print(Employee1)
Employee1.set_name("Joana")
print(Employee1)
