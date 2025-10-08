

import numpy as np 
import time
from multi_diamension_array import array

def PrintAtoZ(array, name_character, prevoius_data):
    for i,layer in enumerate(array):
        for j,row in enumerate(array[i]):            
            for k,char in enumerate(array[i,j]):
                time.sleep(0.02)
                if(char == name_character):
                    print(f"{prevoius_data}{char}")
                    return char
                else: 
                    print(f"{prevoius_data}{char}")

name = input("Enter your name: ").upper()
prevoius_data = ""
array_list = ""
for character in name:
    prevoius_data += PrintAtoZ(array, character, prevoius_data)