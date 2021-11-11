class Person:
    name = 'Ivan'
    age = 30

print(getattr(Person, 'name', 404))
print(getattr(Person, 'x', 404))
setattr(Person, 'x', 100)
print(getattr(Person, 'x', 404))
print(Person.__dict__)
del Person.x
print(Person.__dict__)
print(delattr(Person, 'age'))
print(Person.__dict__)
print(Person.name)

a = Person()
b = Person()

Person.z = 10
print(a.z)