class SavingsAccount:
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__int_rate = int_rate
        self.__bal = bal

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_int_rate(self, int_rate):
        self.__int_rate = int_rate

    def set_bal(self, bal):
        self.__bal = bal

    def get_account_num(self):
        return self.__account_num

    def get_int_rate(self):
        return self.__int_rate

    def get_bal(self):
        return self.__bal


class CD(SavingsAccount):
    def __init__(self, account_num, int_rate, bal, mat_date):
        SavingsAccount.__init__(self, account_num, int_rate, bal)
        self.__mat_date = mat_date

    def set_mat_date(self, mat_date):
        self.__mat_date = mat_date

    def get_mat_date(self):
        return self.__mat_date
