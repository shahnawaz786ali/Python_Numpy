# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

# The probability for the value to be 3 is set to be 0.1

# The probability for the value to be 5 is set to be 0.3

# The probability for the value to be 7 is set to be 0.6

# The probability for the value to be 9 is set to be 0

from numpy import random

arr=random.choice([3,5,7,9], p=[0.2, 0.3, 0.4, 0.1], size=(50))

print(arr)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.

arr1=random.choice([3,5,7,9], p=[0.2, 0.3, 0.4, 0.1], size=(3,5))
print(arr1)


# Same example as above, but return a 3-D array with 3 rows, each containing 5 values.

arr2=random.choice([3,5,7,9], p=[0.2, 0.3, 0.4, 0.1], size=(2,3,5))
print(arr2)