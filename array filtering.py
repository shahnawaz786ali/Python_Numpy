import numpy as np

arr=np.array([90,23,34,27,78,88])

a=[True,False, False,True,True,False]
new_arr=arr[a]

print(new_arr)

# Create a filter array that will return only values higher than 42:
arr1=np.array([90,23,34,27,78,88])

arr2=[]
for i in arr1:
    if i > 42:
        arr2.append(True)

    else:
        arr2.append(False)

new_arr2=arr[arr2]

print(new_arr2)

    
