
class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(self) in self.keys()

str_dict = StrKeyDict([("1", "one"), ("2", "two"), ("3", "three")])
print(str_dict)
print(str_dict["1"])
print(str_dict[2])

print(str_dict.get("1", "N/A"))
print(str_dict.get(1))
print(str_dict.get("2"))
print(str_dict.get(2, "N/A"))
print(str_dict.get(4, "N/A"))
