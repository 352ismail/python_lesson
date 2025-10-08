import numpy as np

# rng = np.random.default_rng(seed=1)
# number = rng.integers(low=1,high=11, size=(4,4))
# print(number)

# np.random.seed(seed =  4)
# number = np.random.uniform(low=2, high=6)
# print(number)


# array = np.array([1,2,3,4,5])
# rng = np.random.default_rng()
# rng.shuffle(array)
# print(array)

fruits =np.array(["🍎", "🍊","🍌", "🍉"])
rng = np.random.default_rng()
fruit = rng.choice(fruits,size=(3,3))

# print(fruit)

# initializing the array of zeros
arr1 = np.zeros((3,3), int)
# print(arr1)

# initializing array of ones
arr2 = np.ones((3,3))
# print(arr2)
# intitalize the identity array 
identity = np.identity(9)
# print(identity)
# create an array from 1-100 do not use any python list or loop in here, just use the numpy array
numbers  = np.arange(1,101,5)
# print(numbers)
data = np.linspace(10,20,10)
print(data)