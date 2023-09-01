import numpy as np

a=np.array([5,6,7,8,9,0])

b=np.array_split(a, 3)

print(b)
print(b[0])
print(b[1])
print(b[2])

c=np.array([[2,3,4],[5,6,7],[7,8,9]])

d=np.array_split(c, 3, axis=1)
e=np.hsplit(c, 3 )
print(p)