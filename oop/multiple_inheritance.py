class Doctor:
    def can_heal(self):
        print('I can heal')

    def can_walk(self):
        print('I am doctor and I can walk')

class Architect:
    def can_build(self):
        print('I can build')

    def can_walk(self):
        print('I am architect and I can walk')

class Person(Doctor, Architect):
    def can_build(self):
        print('I am person and I also can build')
        super().can_walk()

p = Person()
p.can_build()
p.can_heal()
p.can_walk()
print(Person.__mro__)