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






