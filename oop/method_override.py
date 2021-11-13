class Person:
    def __init__(self, name):
        self.name = name

    def can_walk(self):
        print('I can walk')
    
    def can_breathe(self):
        print('I can breathe')

    def can_sleep(self):
        print('I can sleep')

    def combo(self):
        self.can_breathe()
        self.can_walk()
        self.can_sleep()

    def __str__(self):
        return f'Person {self.name}'

class Doctor(Person):
    def can_breathe(self):
        print('Doctor can breathe')

    def __str__(self):
        return f'Doctor {self.name}'

d = Doctor('John')
p = Person('Pasha')
p.can_breathe()
d.can_breathe()
p.can_walk()
d.can_walk()
print(p, d)
d.combo()