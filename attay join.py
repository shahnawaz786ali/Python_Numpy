import numpy as np

a=np.array([4,5,6,7])
b=np.array([8,9,0,4])
arr1=np.array([[2,6,9],[5,7,0]])
arr=np.array([[4,5],[8,9]])
arr2=np.array([[[12,13],[67,77]],[[90,70],[34,19]]])

z=np.concatenate((arr1,arr), axis=1)
y=np.stack((a,b), axis=1)
x=np.hstack((a,b))
h=np.vstack((a,b))
g=np.dstack((a,b))
print(g)