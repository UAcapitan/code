def func1(a,b):
  def func2(c):
    print(str(a+b+c))
  return func2

f1 = func1(10,20)
f1(70)