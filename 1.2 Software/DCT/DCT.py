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

