import decimal

number = decimal.Decimal('1.5')
number += number
print(number)
print(number + 2)

try:
    print(number + 2.0)
except:
    pass

print(number.quantize(decimal.Decimal('1.00')))

number += decimal.Decimal('0.5')

print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_HALF_EVEN)) # стандартное округления класса
print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_HALF_UP)) # математическое округление
print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_DOWN)) # в сторону повышения, если после него идет число больше 5
print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_05UP)) # округляет только 0 до единицы, если после него идет 5
print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_CEILING)) # в большую сторону
print(number.quantize(decimal.Decimal('1.00'), decimal.ROUND_FLOOR)) # не округляет