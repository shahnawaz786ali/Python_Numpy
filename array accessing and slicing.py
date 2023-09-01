import numpy as np

arr1=np.array([2.5,3.6,4.9])
arr2=np.array([[4,9,0],[3,9,0]])  # 2D array
arr3=np.array([[2,7,9],[7,2,5],[6,1,0]]) #2D array

print(arr3)
print(arr3[:1,:2])
print(arr3[1:3,1:3])

# Boolean slicing in nd array
cond= arr2 > 5
temp=arr2[cond]

print(temp)

# integer slicing

temp=arr3[[0,2,1],[2,0, 2]]

print(temp)