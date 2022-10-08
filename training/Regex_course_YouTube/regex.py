'''
    Regex:
        [ab]c - set of symbols, can be "ac" or "bc"
        [^p]c - any, for example "ac" or "bc", except "pc"
        [a-z] - range from "a" to "z"
        [A-Z] - range from "A" to "Z"
        [0-9] - range from 0 to 9
        [a-zA-Z0-9] - range for letters and numbers
        [0-9]+ - endless count of numbers
        [0-9]{11} - 11 numbers

'''


import re


text = "Duck"
regex = r"Duck"

print(bool(re.search(regex, text)))
