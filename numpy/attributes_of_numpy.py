import numpy as np 

numbers = np.array([1,2,3,4,5,6,7,8,9])




# to find all the size of the array 
# print(numbers.size)


# To find number of bytes taken by each element in the array
# print(numbers.itemsize)


# type casting in the array
new_numbers = numbers.astype(str)
print(new_numbers)


# to print the datatype of the array
print(new_numbers.dtype)

# to know how many diamesional array is the current is:
names = np.array([
        [
            ["ismail", "khan"],
            ["ikram", "ali"]
        ],
        [
            ["salman", "khan"],
            ["amir", "khan"]
        ]
    ])
print(names.ndim)
copied_numbers = numbers.copy()
string_numbers = copied_numbers.astype(str)

print(string_numbers)

