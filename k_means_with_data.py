import numpy as np
import matplotlib.pyplot as plt
import random

Data = np.loadtxt(fname='data2.txt')

x = Data[:, 0]
y = Data[:, 1]

col = [[0, 0, 1], [0, 1, 0], [1, 1, 0], [1, 0, 1]]  # RGB values representing colours

n = 3
XC = []
YC = []

IND = []
INDEX = np.arange(0, len(x))
INDEX = INDEX.tolist()

for i in range(n):
    val = np.random.randint(0, len(INDEX))
    ind = INDEX.pop(val)
    IND.append(ind)

XC = x[IND]
YC = y[IND]

plt.plot(x, y, 'o', color='blue')
plt.plot(XC, YC, 'o', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y vs x')
plt.show()

SSE = []
ITR = []
pre_val = 100000
for m in range(1, 10):
    ITR.append(m)
    L = []
    E = []
    for j in range(len(x)):  # cluster centers
        D = np.power((XC - x[j]), 2) + np.power((YC - y[j]), 2)
        L.append(np.argmin(D))  # retrieving the index of the minimum value
        # print(D)
    L = np.array(L)  # converting the list to numpy array

    for k in range(n):
        xarray = []
        yarray = []
        ind = np.where(L == k)
        XC[k] = np.average(x[ind])
        YC[k] = np.average(y[ind])
        xarray = x[ind]
        yarray = y[ind]
        plt.plot(xarray, yarray, 'o', color=col[k])
        plt.plot(XC[k], YC[k], '^', color='red')  # New cluster centers are plotted in triangles
        temp = (np.power((x[ind] - XC[k]), 2) + np.power((y[ind] - YC[k]), 2))
        temp = np.array(temp)
        E.append(np.sum(temp))

    E = np.array(E)
    SSE.append(np.sum(E))
    cur_val = np.sum(E)

    plt.title('Iteration ' + str(m))
    plt.show()
    if (((
                 pre_val - cur_val) / pre_val * 100) < 5):  # Checking whether the different between previous and current E are significant or not.
        break
    pre_val = cur_val

plt.clf()
plt.plot(ITR, SSE, '+', color='blue')
plt.xlabel('Iterations')
plt.ylabel('SSE')
plt.title('SSE vs ITR ')
plt.show()
