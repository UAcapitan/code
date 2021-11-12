class Person:
    def can_walk(self):
        print('I can walk')
    
    def can_breathe(self):
        print('I can breathe')

class Doctor(Person):
    def can_heal(self):
        print('I can heal')
    
class Orthopedist(Doctor):
    def can_heal_his_back(self):
        print('I can heal his back')

class Architect(Person):
    def can_build(self):
        print('I can build')

d = Doctor()
d.can_heal()
d.can_breathe()
d.can_walk()
a = Architect()
a.can_build()
a.can_breathe()
a.can_walk()
o = Orthopedist()
o.can_heal()
o.can_breathe()
o.can_walk()
o.can_heal_his_back()
print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
print(isinstance(d, Doctor))
print(isinstance(d, Person))