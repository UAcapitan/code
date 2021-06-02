class Person:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def sayName(self):
        print(self.getName())

class Robot(Person):
    def __init__(self, name, model):
        super().__init__(name)
        self.__model = model

    def getModel(self):
        return self.__model

    def sayModel(self):
        print(self.getModel())

    def sayNameAndModel(self):
        print(self.getName(), '-', self.getModel(), end=' ')

class NewRobot(Robot):
    def __init__(self, name, model, power):
        super().__init__(name, model)
        self.__power = power

    def setPower(self, power):
        self.__power = power
    
    def getPower(self):
        return self.__power

    def sayPower(self):
        print(self.getPower())

    def sayNameModelPower(self):
        super().sayNameAndModel()
        self.sayPower()

p1 = Person('Kiril')
p1.sayName()

r1 = Robot('Ivan', 'Mi9081i')
r1.sayName()
r1.sayModel()
r1.sayNameAndModel()

nr1 = NewRobot('Petya', 'Ki091ki', 90)
nr1.sayName()
nr1.sayModel()
nr1.sayNameAndModel()
nr1.sayPower()
nr1.sayNameModelPower()