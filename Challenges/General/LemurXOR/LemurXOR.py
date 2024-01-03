from PIL import Image
import numpy as np

def image_to_array(image_path):
    img = Image.open(image_path)
    return np.array(img)

def array_to_image(array, output_path):
    img = Image.fromarray(array)
    img.save(output_path)

flag_path = "flag.png"
lemur_path = "lemur.png"

flag_array = image_to_array(flag_path)
lemur_array = image_to_array(lemur_path)

new_array = np.bitwise_xor(flag_array, lemur_array)

output_path = "new_flag.png"
array_to_image(new_array, output_path)
