
import sys
import re
import pdb
# pdb.set_trace()


WORD_RE = re.compile(r"\w+")

index = {}

with open(sys.argv[1], encoding='utf-8') as file:
    for line_no, line in enumerate(file, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])