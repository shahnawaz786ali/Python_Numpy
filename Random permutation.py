from numpy import random
import numpy as np

arr=np.array([4,7,8,90])

arr1=random.shuffle(arr)    #The shuffle() method makes changes to the original array.

print(arr1)

# Generate a random permutation of elements of following array:

print(random.permutation(arr))  #The permutation() method returns a re-arranged array (and leaves the original array un-changed).
