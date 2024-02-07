class Question:
    def __init__(self, question, answ1, answ2, answ3, answ4, right_answ: int):
        self.__question = question
        self.__answ1 = answ1
        self.__answ2 = answ2
        self.__answ3 = answ3
        self.__answ4 = answ4
        self.__right_answ = right_answ

    def get_question(self):
        return self.__question

    def get_answ1(self):
        return self.__answ1

    def get_answ2(self):
        return self.__answ2

    def get_answ3(self):
        return self.__answ3

    def get_answ4(self):
        return self.__answ4

    def get_right_answ(self):
        return self.__right_answ

    def is_right_answ(self, u_answ):
        return self.__right_answ == u_answ

    def __str__(self):
        return f'{self.__question}\n1. {self.__answ1}.\n2. {self.__answ2}\n3. {self.__answ3}\n4. {self.__answ4}\n'
