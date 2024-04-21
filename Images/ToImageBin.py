




with open("1.2 Software\DCT\SoftwareDCTcat.bin", "rb") as f:
    str_data = f.read()
    data = []
    #print(newstr)
    for d in str_data:
        #print(d)
        data.append(d)
    result_string = ''.join(data)
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
