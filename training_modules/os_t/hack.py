import os

print("192.168.n.---")
n = input("n = ")

for i in range(1, 255):
	os.system(f"ssh 192.168.{n}.{str(i)}")

