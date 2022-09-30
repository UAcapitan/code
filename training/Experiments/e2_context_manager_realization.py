# Original
with open('text.txt', 'w') as file:
    text = 'Just a text'
    file.write(text)

# My realization
class ContextManager():
    def __init__(self, file):
        self.file = file
        print("File was opened")

    def __enter__(self):
        self.file = open(self.file, "w")
        print("Enter is working")
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        del self.file
        print(type)
        print(value)
        print(traceback)
        print("File was closed")

with ContextManager("text.txt") as file:
    file.write("Some text manager")