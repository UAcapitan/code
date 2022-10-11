
import sys
import re


WORD_RE = re.compile(r"\w+")

index = {}

with open(sys.argv[1], encoding='utf-8') as file:
    for line_no, line in enumerate(file, 1):
        for match in WORD_RE.findall(line):
            word = match.group()
            column_no = match.start() + 1

