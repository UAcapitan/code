
import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        print("Data dict")
        print(self.data)
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

str_dict = StrKeyDict([("1", "one"), ("2", "two"), ("3", "three")])
print(str_dict)
print(str_dict["1"])
print(str_dict[2])

print(str_dict.get("1", "N/A"))
print(str_dict.get(1))
print(str_dict.get("2"))
print(str_dict.get(2, "N/A"))
print(str_dict.get(4, "N/A"))

print("1" in str_dict)
print(1 in str_dict)
