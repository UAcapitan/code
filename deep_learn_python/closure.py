age = 27
def birthday(): 
  age = 28
birthday()
print(age)

def countdown(start):
  def display():
    n = start
    while n > 0:
      n -= 1
      print('T-minus %d' % n)
 
  display()
countdown(3)

def countdown(start):
  def display():
    n = start
    while n > 0:
      n -= 1
      print('T-minus %d' % n)
  return display

counter1 = countdown(2)
counter1()