# Class for create object - car
class Toyota:

    def __init__(self):
        self.color = 'Burgundy matallic'
        self.price = '1 000 000 rub'
        self.max_velocity = '200 km/h'
        self.current_velocity = '0 km/h'
        self.engine_rpm = 0

    def start(self):
        print('Motor started')
        self.engine_rpm = 900

    def go(self):
        print('Go!')
        self.engine_rpm = 2000
        self.current_velocity = '20 km/h'

my_car = Toyota()
print('color', my_car.color)
print('price', my_car.price)
print('max_velocity', my_car.max_velocity)
print('rmp', my_car.engine_rpm)
print('current_velocity', my_car.current_velocity)

my_car.start()
print('rmp', my_car.engine_rpm)

my_car.go()
print('rpm', my_car.engine_rpm)
print('current_velocity', my_car.current_velocity)

# Create list cars
produced, plan = 0, 10000
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced += 1

# Class for create object - robor
class Robot:
    """Simple example class"""

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Hello, world! I am', self.name)

robot = Robot()
robot.hello()

some_var = robot
some_var.hello()

some_robot = some_var
some_robot.hello()

some_robot.name = 'C-3PO'
some_robot.hello()

robot.hello()