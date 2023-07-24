
import os


files = os.listdir()
for file in files:
    if file == "env":
        continue
    os.rename(file, "e" + file)
