import numpy as np

arr=np.ones((3,3), dtype=np.int64)
arr1=np.zeros((2,2), dtype=np.int64)

arr2=np.full((4,4), 5, dtype=np.int64)

arr3=np.arange(0,9).reshape(3,3)

print(arr1)
print(arr)
print(arr2)
print(arr3)