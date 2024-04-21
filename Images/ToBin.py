'''

Taking an image and turning it into a .bin file 

'''

import base64



print("Converting Image to string")

with open("cat.png", "rb") as image2string: 
    converted_string = base64.b64encode(image2string.read()) 
    #print(converted_string) 

with open('cat.bin', "wb") as file: 
        file.write(converted_string)




