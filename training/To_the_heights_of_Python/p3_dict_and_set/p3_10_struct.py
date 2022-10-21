
import struct

fmt = "<3s3sHH"

with open("img.gif", "rb") as file:
    img = memoryview(file.read())

header = img[:10]
print(header)

print(bytes(header))
print(struct.unpack(fmt, header))

del header
del img
