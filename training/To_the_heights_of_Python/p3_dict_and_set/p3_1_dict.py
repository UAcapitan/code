
a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(["one", "two", "three"], [1, 2, 3]))

print(a == b == c)


# List with tuples to dict
CODES = [
    ("003", "Green"),
    ("007", "Light green"),
    ("017", "Dark green")
]

result_dict = {code: color for code, color in CODES}

print(result_dict)
