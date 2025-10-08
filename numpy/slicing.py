import numpy as np

array = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])

#array[start:end:step]
# print(array[2:,2:])


# make it 3*3 metrix and sum the diagonal
# duplicated_metrix = array[0:3,0:3]
# print(f"3x3 metrix: \n{duplicated_metrix}")

# #find sum of the diagonal: 
# total = 0
# for i,row in enumerate(duplicated_metrix):
#     for j,num in enumerate(row):
#         if(i==j):
#             total+= num
# print(total)



# #find sum of the first column: 
# first_column = array[:,0]
# total = 0
# for row in first_column:
#     total += row
# print(total)

#find the reverse diagonal sum 
# total = 0
# array = array[::-1]
# for i,rows in enumerate(array):
#     for j,num in enumerate(rows):
#         if i == j:
#             total += num
# print(total)