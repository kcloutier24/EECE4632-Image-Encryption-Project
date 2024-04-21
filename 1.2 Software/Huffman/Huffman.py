
'''

Taking an image and turning it into a .bin file 

'''

import base64



print("Converting Image to string")

with open("Images\cat.png", "rb") as image2string: 
    converted_string = base64.b64encode(image2string.read()) 
    
    

    #print(converted_string) 

with open('1.2 Software\Huffman\Softwarecat.bin', "wb") as file: 
        file.write(converted_string)



with open("1.2 Software\Huffman\Softwarecat.bin", "rb") as f:
    binary_data = f.read()
    #print("Binary values of the data:")
    out = []
    for b in binary_data:
        #print(b)
        out.append(b)
    #print(binary_data)
    #print(out)
        
print("Readng test in, raw data")


with open("1.2 Software\Huffman\SoftwarecatData.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out, numbers")




with open("1.2 Software\Huffman\SoftwarecatData.bin", "rb") as f:
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

with open("1.2 Software\Huffman\SoftwarecatDataSegmented.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out, numbers")












########################################################################################################################################



import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def encode_huffman(root, code="", mapping=None):
    if mapping is None:
        mapping = {}
    if root is None:
        return

    if root.char is not None:
        mapping[root.char] = code
        return

    encode_huffman(root.left, code + "0", mapping)
    encode_huffman(root.right, code + "1", mapping)

    return mapping

def huffman_encode(text):
    root = build_huffman_tree(text)
    mapping = encode_huffman(root)
    encoded_text = ''.join(mapping[char] for char in text)
    return encoded_text, mapping

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_encoded_file(encoded_text, encoding_map, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(encoded_text)
        file.write("\n")
        for char, code in encoding_map.items():
            file.write(f"{char}:{code}\n")

# Read content from the text file
file_path = "1.2 Software\Huffman\Softwarecat.bin"
text_content = read_text_file(file_path)

# Encode the content using Huffman encoding
encoded_text, encoding_map = huffman_encode(text_content)

# Write the encoded content and encoding map to a new file
output_file_path = "1.2 Software\Huffman\SoftwareHuffcat.bin"
write_encoded_file(encoded_text, encoding_map, output_file_path)

print("Encoded file has been created:", output_file_path)

########################################################################################################################################













with open("1.2 Software\Huffman\SoftwareHuffcat.bin", "rb") as f:
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


with open("1.2 Software\Huffman\SoftwareHuffmancatDataImage.bin", "w") as f:
    f.write((decrypted_string))



print("Writing to test image, raw data format")




'''


Takes .bin file after encoding and turns it back into an image

'''

import numpy as np
from PIL import Image

# Path to the binary file
bin_file_path = "1.2 Software\Huffman\SoftwareHuffmancatDataImage.bin"

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
image.save("Images/Software/SoftwareHuffmancat.png")













