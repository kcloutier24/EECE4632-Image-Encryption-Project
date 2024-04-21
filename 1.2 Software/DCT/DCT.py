'''

Taking an image and turning it into a .bin file 

'''

import base64



print("Converting Image to string")

with open("Images\cat.png", "rb") as image2string: 
    converted_string = base64.b64encode(image2string.read()) 
    
    

    #print(converted_string) 

with open('1.2 Software\DCT\Softwarecat.bin', "wb") as file: 
        file.write(converted_string)



with open("1.2 Software\DCT\Softwarecat.bin", "rb") as f:
    binary_data = f.read()
    #print("Binary values of the data:")
    out = []
    for b in binary_data:
        #print(b)
        out.append(b)
    #print(binary_data)
    #print(out)
        
print("Readng test in, raw data")


with open("1.2 Software\DCT\SoftwarecatData.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out, numbers")




with open("1.2 Software\DCT\SoftwarecatData.bin", "rb") as f:
    str_data = f.read()
    data = []
    newstr = str_data.decode()
    #print(newstr)
    for d in newstr:
        #print(d)
        data.append(d)
    result_string = ''.join(data)
    #print(result_string)

print("Reading test out")


'''
separates it again

'''

# Initialize an empty list to store the segments
segmented_list = []

# Iterate through the original string
i = 0
while i < len(result_string):
    # Take a substring of length 2 or 3
    segment_length = 2 if i + 2 <= len(result_string) else 3
    segment = result_string[i:i+segment_length]
    # Append the segment to the list
    segmented_list.append(segment)
    # Update the index for the next iteration
    i += segment_length

#print(segmented_list)

print("Segmented")

with open("1.2 Software\DCT\SoftwarecatDataSegmented.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out, numbers")




import numpy as np
import cv2

def dct_encode(input_file, output_file):
    
    with open(input_file, 'rb') as f:
        binary_data = f.read()
    
    
    data_array = np.frombuffer(binary_data, dtype=np.uint8)
    
    
    height = int(np.sqrt(len(data_array)))
    width = height
    data_array = data_array[:height*width]
    data_array = data_array.reshape((height, width))
    
    # D DCT
    dct_encoded_data = cv2.dct(np.float32(data_array))

    # Save the DCT encoded data to a new binary file
    with open(output_file, 'wb') as f:
        f.write(dct_encoded_data.tobytes())

# Example usage
input_file = '1.2 Software\DCT\SoftwarecatData.bin'
output_file = '1.2 Software\DCT\SoftwareDCTcat.bin'
dct_encode(input_file, output_file)
print("dct encoded")






with open("1.2 Software\DCT\SoftwareDCTcat.bin", "rb") as f:
    str_data = f.read()
    data = []
    #print(newstr)
    for d in str_data:
        #print(d)
        data.append(d)
# Convert integers to strings before joining
result_string = ''.join(str(item) for item in data) #fucking keep it like this
    #print(result_string)

print("Reading test out")








# Convert ASCII values to characters or integers
decrypted_string = ''.join(chr(int(value)) if (32 <= int(value) <= 126) or (48 <= int(value) <= 57) or value in ['94', '94', '94', '61', '94'] else value for value in result_string)

print("Decrypted string")
#print(decrypted_string)

#binary_data = decrypted_string.encode()


with open("1.2 Software\DCT\SoftwareDCTcatDataImage.bin", "w") as f:
    f.write((decrypted_string))



print("Writing to test image, raw data format")




'''


Takes .bin file after encoding and turns it back into an image

'''

import numpy as np
from PIL import Image

# Path to the binary file
bin_file_path = "1.2 Software\DCT\SoftwareDCTcatDataImage.bin"

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











