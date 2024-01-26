class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age =age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def receive_data():
    name = input('Enter animal\'s name')
    animal_type = input('Enter animal\'s type')
    age = input('Enter animal\'s age')
    return name, animal_type, age

animal1 = Pet(*receive_data())
animal2 = Pet(*receive_data())
animal3 = Pet(*receive_data())

print(animal1.get_name())
animal1.get_animal_type()
animal1.get_age()

animal2.get_name()
print(animal2.get_animal_type())
animal2.get_age()

animal3.get_name()
animal3.get_animal_type()
animal3.get_age()
