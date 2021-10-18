print_str = 'print("Hello, world")'

exec(print_str)
eval(print_str)

nums = '10 + 5'

print(eval(nums))
print(exec(nums))

variable = 'x = 10'

exec(variable)
exec('print(x)')
try:
    eval(variable)
except:
    pass

code1 = 'x = 5\nx+=5\nprint(x)'

exec(code1)
try:
    eval(code1)
except:
    pass

code2 = 'def addNum(x):\n    return x + 5\nprint(addNum(5))'

exec(code2)
try:
    eval(code2)
except:
    pass