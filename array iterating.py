import numpy as np

arr=np.array([4,5,6,7])
arr1=np.array([[2,6,9],[5,7,0]])
arr2=np.array([[[12,13],[67,77]],[[90,70],[34,19]]])

'''
for x in arr:
    print(x)
 
for x in arr1:
    for y in x:
        print(y)

for x in arr2:
    for y in x:
        for z in y:
            print(z)
'''

# second method
for x in np.nditer(arr2):
    print(x)


# Enumerate method
for x in np.ndenumerate(arr2):
    print(x)


