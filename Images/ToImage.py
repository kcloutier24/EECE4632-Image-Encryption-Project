'''


Takes .bin file after encoding and turns it back into an image

'''

import numpy as np
from PIL import Image

# Path to the binary file
bin_file_path = "1.2 Software\DCT\SoftwarecatData.bin"

width = 100
height = 100

with open(bin_file_path, 'rb') as f:
    binary_data = f.read()

pixel_values = np.frombuffer(binary_data, dtype=np.uint8)

expected_size = width * height
if len(pixel_values) != expected_size:
    pixel_values = np.resize(pixel_values, expected_size)

image_data = np.reshape(pixel_values, (height, width))

image = Image.fromarray(image_data)




print("Image formed from image data")
image.save("Images/Software/SoftwareDCTcat.png")
