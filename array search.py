import numpy as np

arr=np.array([2,3,4,5,6,7,9])

a=np.where(arr==5) 
print(a)

# Find the indexes where the values are even:
arr=np.array([2,3,4,5,6,7,9])

print(np.where(arr%2 == 0))

# Find the indexes where the values are odd:
arr=np.array([2,3,4,5,6,7,9])

print(np.where(arr%2 == 1))

# Find the indexes where the value 7 should be inserted:

arr1=np.array([3,6,8,7])

print(np.searchsorted(arr1, 7))


# Find the indexes where the value 7 should be inserted, starting from the right:
arr2=np.array([3,6,8,7])

print(np.searchsorted(arr2, 7, side="right"))
