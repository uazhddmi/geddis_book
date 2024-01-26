# tax rate for sales
TAX_RATE = 0.05

class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__pcharge = pcharge
        self.__lcharge = lcharge

    def set_parts_charges(self, pcharge):
        self.__pcharge = pcharge

    def set_labor_charges(self, lcharge):
        self.__lcharge = lcharge

    def get_parts_charges(self):
        return self.__pcharge

    def get_labor_charges(self):
        return self.__lcharge

    def get_sales_tax(self):
        return self.__pcharge * TAX_RATE

    def get_total_charges(self):
        return self.__pcharge + self.__lcharge + \
            (self.__pcharge * TAX_RATE)
