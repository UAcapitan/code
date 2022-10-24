
from unicodedata import name, normalize


ohm = '\u2126'
print(name(ohm))

ohm = normalize('NFC', ohm)
print(name(ohm))
