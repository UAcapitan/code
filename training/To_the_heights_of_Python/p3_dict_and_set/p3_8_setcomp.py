
from unicodedata import name


set_ = {chr(i) for i in range(32,256) if "SIGN" in name(chr(i), "")}
print(set_)
