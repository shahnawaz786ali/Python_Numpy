import numpy as np

arr=np.array([4,5,6,7],dtype="i")

arr1=arr.copy()  # return new array
arr2=arr.view()  # allow view of array

arr2[2]=10
print(arr1)
print(arr2)
print(arr)