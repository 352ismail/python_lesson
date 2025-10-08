# if the number of rows are the same, or one of them is 1 then broadcasting can be done. 
# if the number of columns are same, or one of them is 1 then braodcastig can be done.

import numpy as np 
A = np.array([[1,2,3,4,5,6,7,8,9,10]])
B = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])


print(A*B)

