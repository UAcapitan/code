
from PIL import Image
import io


# First way
def image_to_byte_array(name: str) -> bytes:
    with open(name, "rb") as file:
        contents = file.read()

    return contents

# Second way
def image_to_byte_array_module(image: Image) -> bytes:
  img_byte_arr = io.BytesIO()
  image.save(img_byte_arr, format=image.format)
  img_byte_arr = img_byte_arr.getvalue()

  return img_byte_arr


if __name__ == "__main__":
    result = image_to_byte_array("image.png")
    result_module = image_to_byte_array_module(Image.open("image.png", "r"))
    
    print(result, "\n\n", result_module)
