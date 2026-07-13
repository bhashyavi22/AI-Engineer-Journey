# program 1 - reshape

import numpy as np
arr=np.array([1,2,3,4,5,6])
new_arr=arr.reshape(3,2)
print(new_arr)
print("-------------------------------")

# program 2 - dimension(-1) (calculate dimension automatically)


arr=np.array([1,2,3,4,5,6])
new_arr=arr.reshape(2,-1)
new_arr1=arr.reshape(-1,3)
print(new_arr)
print()
print(new_arr1)
print("-------------------------------")

#program 3 - flatten(converts multidimensional array to 1D array)

import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])
new_arr=arr.flatten()
print(new_arr)
print()
#if you change the flattened array ,the original array does not change
import numpy as np
arr = np.array([[1, 2],
                [3, 4]])
flat = arr.flatten()
flat[0] = 100
print(flat)
print(arr)
print("----------------------------")

# program 4 - ravel

import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
new_arr=arr.ravel()
print(new_arr)
print()

#if you change ravel array,the original array also changed
import numpy as np
arr = np.array([[1, 2],
                [3, 4]])
new_arr = arr.ravel()
new_arr[0] = 100
print(new_arr)
print(arr)