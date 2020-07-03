import numpy as np

a = np.random.randn(5)

print(a)

print(a.shape)

#transpose
print(a.T)

#inner product between a and a transpose
print(np.dot(a,a.T))

a = np.random.randn(5,1)
print(a)

print(a.T)

#outer product of vector
print(np.dot(a,a.T))


