class Robot:
    """Simple example class"""

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Hello, world! I am', self.name)

    def go(self, x, y):
        print('Go in', x, y)

robot = Robot()
robot.temperature = 1

while robot.temperature < 10:
    robot.temperature *= 2
print(robot.temperature)
del robot.temperature

robot_2 = Robot()
robot_2.name = 'C-77I1'

print(robot.name, robot_2.name)

print(robot == robot_2)

attr_name_1 = 'name'
attr_name_2 = 'model'

if hasattr(robot, attr_name_1):
    print(robot.name)
elif hasattr(robot, attr_name_2):
    print(robot.model)
else:
    setattr(robot, attr_name_1, 'C1')
    setattr(robot, attr_name_2, 'Io')
    print('Objects haven`t attrs')

    print(getattr(robot, attr_name_1))
    print(getattr(robot, attr_name_2))

    delattr(robot, attr_name_2)

robot.go(x=10, y=20)