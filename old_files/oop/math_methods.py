class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        self.__balance = value

    def __add__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = self.my_balance + other.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = self.my_balance + other
            return self.my_balance
        raise NotImplemented
    
    def __radd__ (self, other):
        return self+other

    def __mul__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = self.my_balance * other.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = self.my_balance * other
            return self.my_balance
        if isinstance(other, str):
            return str(self.my_balance) + other
        raise NotImplemented

    def __rmul__(self, other):
        return self*other

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = self.my_balance - other.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = self.my_balance - other
            return self.my_balance
        raise NotImplemented

    def __rsub__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = other.my_balance - self.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = other - self.my_balance
            return self.my_balance
        raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = self.my_balance / other.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = self.my_balance / other
            return self.my_balance
        raise NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, BankAccount):
            self.my_balance = other.my_balance / self.my_balance
            return self.my_balance
        if isinstance(other, (int, float)):
            self.my_balance = other / self.my_balance
            return self.my_balance
        raise NotImplemented

r = BankAccount('Misha', 78)
b = BankAccount('Tanya', 900)
print(r+20)
print(r.my_balance)
print(r+b)
print(r.my_balance)
print(b.my_balance)
# print(r+'P')
print(12+r)
print(r*2)
print(r*b)
print(2*r)
print(r*'$')
print(r.my_balance)
print(r-2)
print(r-b)
print(2-r)
print(r/2)
print(r/b)
print(2/r)