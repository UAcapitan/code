
from array import array

symbols = "$%*#&^!"

array_symbols = array('I', [ord(symbol) for symbol in symbols])
array_symbols.append(1)
print(array_symbols)
