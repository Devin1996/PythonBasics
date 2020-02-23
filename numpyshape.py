import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

b = np.array([[1,2,3],[4,5,6]])
c=b.reshape(3,2)
print(c)

d = np.arange(24)
print(d)

e=d.reshape(8,3)
print(e)

f=d.reshape(2,4,3)

print(f)