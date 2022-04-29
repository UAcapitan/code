class Func:
    @classmethod
    def print_name(cls, name):
        print(name)
        return True
    
    @staticmethod
    def print_age(age):
        print(age)
        return True

Func.print_name('Ivan')
Func.print_name(10)