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
        [0-9]{5,8} - count range from 5 to 8
        [0-9]{5,} - 5 symbols is minimum
        ^[0-9]{3}$ - begin and end for searching needed match
        (a|b)c - there are "ac" or "bc"

    Metasymbols:
        \d - [0-9]
        \w - [a-zA-Z0-9_]
        \s - space, tab, etc.
        \t - only tabs

    Special symbols:
        ? - optional
        . - any symbol
        * - 0 or any amount of symbols
'''

import re


# Search in text
text = "Duck"
regex = r"Duck"
result = re.search(regex, text)
print(result)
print(bool(result))
print(result.span())
print(result.string)
print(result.group())

print()

# Fullmatch with text
print(re.fullmatch(regex, text))

print()

text = "I don't know 5.55. There are some 7.09 text. So I hope you can find 19.00 need information for you here."

# RegEx compilation
regex = re.compile(r"\d{1,}\.\d{2,}")

# Find all matches
print(re.findall(regex, text))

# Split by matches
print(re.split(regex, text))

# Replace with matches
print(re.sub(regex, "_.__", text))
