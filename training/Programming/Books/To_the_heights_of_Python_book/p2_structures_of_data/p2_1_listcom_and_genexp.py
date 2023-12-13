
symbols = "$%*#&^!"

codes1 = []
for symbol in symbols:
    codes1.append(ord(symbol))

codes2 = [ord(symbol) for symbol in symbols]
codes3 = (ord(symbol) for symbol in symbols)
print(codes1 == codes2)
print(codes2 == codes3)

for i in codes3:
    print(i)

tuple_symbols = tuple(ord(symbol) for symbol in symbols)
print(tuple_symbols)
print(tuple_symbols == codes3)
