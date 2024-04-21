'''

Testing the idea of sending in a large number all together then turn it into an array in hardware, 
mix it up, turn it back into one big number, send it back, break it up into an array, then decode it



'''



'''
turng the .bin into an array


'''

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


with open("Test/testout.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out, numbers")



'''


with open("3. ProjectRevisited/testout.bin", 'rb') as f_in:
    with open("3. ProjectRevisited/testoutadd.bin", 'wb') as f_out:
        while True:
            # Read 8 bytes (2 integers assuming each integer is 4 bytes)
            chunk = f_in.read(8)
            if not chunk:
                break  # Reached end of file
                # Convert binary data to two integers
            int1 = int.from_bytes(chunk[:4], byteorder='little')
                # Add 5 to each integer
            modified_int1 = int1 + 5
                # Convert modified integers back to binary data and write to output file
            f_out.write(modified_int1.to_bytes(4, byteorder='little'))
            
print("Wirring to test out add five")


with open("3. ProjectRevisited/testoutadd.bin", "rb") as f:
    binary_data = f.read()
    #print("Binary values of the data:")
    out = []
    for b in binary_data:
        #print(b)
        out.append(b)
    #print(binary_data)
    #print(out)
        
print("Readng test add in, raw data")


with open("3. ProjectRevisited/testoutadd.bin", "w") as f:
    for te in binary_data:
        f.write(str(te))

print("Writting to test out add, numbers")



'''








'''

joins everything making it one big thing

'''



with open("Test/testout.bin", "rb") as f:
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





'''
adds in characters

'''
# Original list of ASCII values as strings
#ascii_values = ['10', '67', '71', '07', '70', '10', '26', '61', '21', '10', '31', '12', '74', '68', '85', '12', '08', '94', '87', '49', '77', '51', '21', '11', '91', '09', '80']

# Convert ASCII values to characters or integers
decrypted_string = ''.join(chr(int(value)) if (32 <= int(value) <= 126) or (48 <= int(value) <= 57) or value in ['94', '94', '94', '61', '94'] else value for value in segmented_list)

print("Decrypted string")
#print(decrypted_string)

#binary_data = decrypted_string.encode()


with open("Test/testimage.bin", "w") as f:
    f.write((decrypted_string))



print("Writing to test image, raw data format")


'''


'''
