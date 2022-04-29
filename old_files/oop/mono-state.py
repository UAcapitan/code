class Car:

    __shared_attr = {
        'model': 'BMW',
        'color': 'white'
    }

    def __init__(self):
        self.__dict__ = Car.__shared_attr

a1 = Car()
print(a1.model)
a1.model, a1.color = 'Tesla', 'green'
print(a1.model)
a2 = Car()
print(a1.model)
print(a2.model)
a2.model, a2.color = 'Lada', 'pink'
print(a1.model)
print(a2.model)