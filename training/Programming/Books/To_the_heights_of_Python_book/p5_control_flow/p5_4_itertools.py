
import itertools


print("Combinations:")
for i in itertools.combinations("ABC", 2):
    print(i)
print()

print("Combinations with replacements:")
for i in itertools.combinations("ABCDEFG", 3):
    print(i)
print()

print("Count:")
for i in itertools.count(1, 2):
    print(i)
    if i > 15:
        break
print()

print("Cycle:")
n = 0
for i in itertools.cycle([1,2,3]):
    print(i)
    if n == 7:
        break
    n += 1
print()

print("Permutations:")
for i in itertools.permutations("ABC", 2):
    print(i)
print()

print("Repeat:")
for i in itertools.repeat("Hi!", 3):
    print(i)
print()

print("Group by:")
for i in itertools.groupby([1,2,3,4,5,6,7], lambda x: x < 3):
    print(i)
print()

print("Tee:")
for i in itertools.tee([1,2,3], 3):
    print(i)
print()
