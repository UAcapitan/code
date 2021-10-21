import collections

# Counter -----------------------------------------------------
l = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']
c = collections.Counter(l)
s = set(c)
print(s)
print(c)
for i,j in c.items():
    print(str(i) + ' - ' + str(j))

c = collections.Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

c = collections.Counter('Python is really cool').most_common(5)
print(c)

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

l = 'I am programmer'
c = collections.Counter(l)
print(sum(c.values()))
print(list(c))
print(c.most_common()[::-1])
c = collections.Counter(a=4, b=2, c=0, d=-2)
print(c)
c += collections.Counter()
print(c)
c.clear()
print(c)