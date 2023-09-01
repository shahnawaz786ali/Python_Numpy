#Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import *

arr=random.randint(100, size=(5))
print(arr)


# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

arr1=random.randint(50, size=(2,3))

print(arr1)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
arr2=random.choice([3,5,7,9], size=(3,2))

print(arr2)