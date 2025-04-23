import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    #1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    #2. Добавь товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items = self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self.__name_items = self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price(item))
        amount = sum(total)

        if len(self.__name_items) > 10:
            amount *= 0.9
        return amount
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        amount = sum(total)
        if len(self.__name_items) > 10:
            amount *= 0.9
        
        return amount * 0.2
        

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item]) 

        amount = sum(total)
        if len(self.__name_items) > 10:
            amount *= 0.9

        return amount * 0.1


    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        number_str = str(telephone_number)
        if len(number_str) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{number_str}'
