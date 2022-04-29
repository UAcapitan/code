class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)
        self.__print_greets()

    def __print_greets(self):
        print('Hello')

account1 = BankAccount('Bob', 10000, 89793792)
# account1.print_public_data()
# account1.print_protected_data()
account1.print_private_data()
# account1.__print_greets()
# account1._BankAccount__print_greets()