class Bank:
    def __init__(self, name, balance):
        self.__name = balance
        self.__balance = balance

    @property
    def my_balance(self):
        print(self.__balance)

    @my_balance.setter
    def my_balance(self, value):
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

account1 = Bank('Kiril', 100)
account1.my_balance
account1.my_balance = 101
account1.my_balance
del account1.my_balance
# account1.my_balance
