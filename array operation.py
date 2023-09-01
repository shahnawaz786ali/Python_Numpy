import numpy as np

arr2=np.array([[4,9,0],[3,9,0]])
arr3=np.array([[2,7,9],[7,2,5]])

print(arr2 + 1)
print(arr3 - 1)
print(arr2 + arr3)

print(arr2.sum())
print(arr2.max())
print(arr2.min())

print(arr2**2)

print(arr2.shape)
print(arr2.ndim)

print(arr2.max(axis=1))
print(arr2.max(axis=0))


