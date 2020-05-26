import numpy as np
import matplotlib.pyplot as plt
import random

x = np.array([8, 5, 3, 9, 6, 7, 6, 4, 4, 3, 1, 2])
y = np.array([5, 4.6, 7.4, 1.4, 1.9, 5.5, 3.5, 9.2, 1.8, 3, 7.8, 6])

n = 2
XC = [2, 7]
YC = [5, 8]

plt.plot(x, y, 'o', color='blue')
plt.plot(XC, YC, 'o', color='red')
plt.xlabel('Frequency')
plt.ylabel('Amount in x 1000 Euros')
plt.title('Amount Spent vs Frequency of Purchases')
plt.show()

SSE = []
ITR = []
pre_val = 1000
for m in range(1, 10):
    ITR.append(m)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for j in range(len(x)):  # cluster centers
        Dis = []
        for k in range(n):
            D = np.power((XC[k] - x[j]), 2) + np.power((YC[k] - y[j]), 2)
            Dis.append(D)
        if (Dis[0] < Dis[1]):
            x1.append(x[j])
            y1.append(y[j])
        else:
            x2.append(x[j])
            y2.append(y[j])

    x1 = np.array(x1)
    x2 = np.array(x2)
    y1 = np.array(y1)
    y2 = np.array(y2)

    XC[0] = np.average(x1)
    XC[1] = np.average(x2)
    YC[0] = np.average(y1)
    YC[1] = np.average(y2)

    plt.plot(x1, y1, 'o', color='blue')
    plt.plot(XC[0], YC[0], '^', color='blue')
    plt.plot(x2, y2, 'o', color='red')
    plt.plot(XC[1], YC[1], '^', color='red')
    plt.title('Iteration ' + str(m))
    plt.show()

    D1 = (np.power((x1 - XC[0]), 2) + np.power((y1 - YC[0]),
                                               2))  # Distance squared from each point in cluster 1 to its center
    D2 = (np.power((x2 - XC[1]), 2) + np.power((y2 - YC[1]),
                                               2))  # Distance squared from each point in cluster 2 to its center
    D1 = np.array(D1)
    D2 = np.array(D2)

    SSE_value = np.sum(D1) + np.sum(D2)
    SSE.append(SSE_value)
    cur_val = SSE_value

    if (((
                 pre_val - cur_val) / pre_val * 100) < 5):  # Checking whether the different between previous and current E are significant or not.
        break
    pre_val = cur_val

plt.plot(ITR, SSE, '+', color='blue')
plt.xlabel('Iterations')
plt.ylabel('SSE')
plt.title('SSE vs ITR ')
plt.show()