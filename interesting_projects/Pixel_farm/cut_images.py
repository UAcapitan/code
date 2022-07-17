import os
from PIL import Image

list_ = os.listdir(f"{os.getcwd()}/src")

for i in list_:
    list_element = os.listdir(f"{os.getcwd()}/src/{i}")
    print(list_element)
    for j in list_element:
        address = f"{os.getcwd()}/src/{i}/{j}"
        im = Image.open(address)
        im1 = im.crop((0, 0, 64, 64))
        os.remove(address)
        im1.save(address)