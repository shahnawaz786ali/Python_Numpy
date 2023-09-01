import numpy as np

arr=np.array([[[2,3],[3,3]],[[1,1,],[8,9]]])
arr1=np.full((2,4,3), 3,dtype=np.int64)
arr2=np.arange(6,dtype=np.int32).reshape(2,3)
arr3=np.array([2,3,4,5,6],dtype=np.int32)

print(arr3[3])
print(arr[0, 1, 1])
print(arr2[0,2])
