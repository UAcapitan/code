class Person:
    def walk(self):
        print('I can walk')

    def combo(self):
        self.walk()
        if hasattr(self, 'sleep'):
            self.sleep()

class Doctor(Person):
    def sleep(self):
        print('Doctor can sleep')

p = Person()
d = Doctor()
p.combo()
print('-'*10)
d.combo()