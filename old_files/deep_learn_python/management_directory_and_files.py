import os

# Get current directory
print(os.getcwd())
print(os.getcwdb())

# Changing directory
os.chdir('D:\\')
print(os.getcwd())

# List directories and files
print(os.listdir())
print(os.listdir('C:\\'))

# Making a new directory
os.mkdir('New')
os.chdir('D:\\New')
print(os.getcwd())

with open('file.txt','w') as file:
    file.write('Hello, wolrd!')

print(os.listdir())

# Renaming a directory or file
os.rename('file.txt', 'f.txt')
print(os.listdir())

# Removing directory or file
os.remove('f.txt')
print(os.listdir())

os.chdir('D:\\')
os.rmdir('New')
print(os.listdir())