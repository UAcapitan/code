class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a2 = Car()

print(a1.model)
print(a2.engine)
print(a1.__dict__)
a1.name = 'Cool car'
print(a1.__dict__)
a1.model = 'Lada'
print(a1.__dict__)
del a1.model
print(a1.__dict__)