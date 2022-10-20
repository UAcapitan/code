
b = bytes('cafe', encoding='utf-8')

print(b)

print(b[0])
print(b[:1])
print(b[1])
print(b[1:2])

b_arr = bytearray(b)
print(b_arr)

print(b_arr[-1:])
print(b_arr[:-1])
print(b_arr[0])
