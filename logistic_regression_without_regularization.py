# This program is about an example of Logistic Regression without Regularization

import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt(fname='Training_Data.txt')
X1 = Data[:, 0]  # Feature-1
X2 = Data[:, 1]  # Feature-2
Y = Data[:, 2]  # Classes

n = int(len(X1) / 2)  # Half of the data is in class 1 (100 points) *known fact.
# Other half in class 2.
m = 2 * n  # No. of data points in total  (100+100)

X0 = np.ones(m)  # 1-D vector having 200 elements with value one
X = np.zeros((3, m))  # 3 * 200 matrix with zeros as the elements
X[0] = X0
X[1] = X1
X[2] = X2

theta0 = 1
theta1 = 1
theta2 = 1
THETA = np.zeros((3, 1))  # 3 x 1 matrix
THETA[0] = theta0
THETA[1] = theta1
THETA[2] = theta2

H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))  # [[ 1 x 200 ]]
H = H.ravel()  # []  1-D vector
COST = (-1 / m) * np.sum(np.multiply(Y, np.log(H)) + np.multiply((1 - Y), np.log(1 - H)))

itr = 1000
E = np.zeros(itr)
THETA_VEC = np.zeros((1, 3))  # 1 x 3 matrix
for i in range(1, itr):  # Appending 999 times
    THETA_VEC = np.append(THETA_VEC, np.zeros((1, 3)), axis=0)

alpha = 0.1
for i in range(0, itr):
    theta0 = theta0 - alpha * (1 / m) * np.sum((np.multiply((H - Y), 1)))
    theta1 = theta1 - alpha * (1 / m) * np.sum((np.multiply((H - Y), X1)))
    theta2 = theta2 - alpha * (1 / m) * np.sum((np.multiply((H - Y), X2)))
    THETA_VEC[i][0] = theta0
    THETA_VEC[i][1] = theta1
    THETA_VEC[i][2] = theta2
    THETA[0] = theta0
    THETA[1] = theta1
    THETA[2] = theta2
    H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))  # [ [ ] ]
    H = H.ravel()  # converting to  [] form
    COST = (-1 / m) * np.sum(np.multiply(Y, np.log(H)) + np.multiply((1 - Y), np.log(1 - H)))
    E[i] = COST

ind = np.argmin(E)
minV = E[ind]
theta0 = THETA_VEC[ind][0]
theta1 = THETA_VEC[ind][1]
theta2 = THETA_VEC[ind][2]
THETA[0] = theta0
THETA[1] = theta1
THETA[2] = theta2

H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))
H = H.ravel()  # converting to [] form
H = np.round(H)
c1_x1 = []
c1_x2 = []
c2_x1 = []
c2_x2 = []
for i in range(0, m):
    temp_x1 = X1[i]
    temp_x2 = X2[i]
    val = H[i]
    if val == 0:
        c1_x1.append(temp_x1)
        c1_x2.append(temp_x2)
    else:
        c2_x1.append(temp_x1)
        c2_x2.append(temp_x2)

plt.figure()
plt.subplot(131)
plt.plot(X1[0:n], X2[0:n], '.', color='blue', markersize=3)
plt.plot(X1[n:m], X2[n:m], '.', color='red', markersize=3)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Training Data')

plt.subplot(132)
plt.plot(X1[0:n], X2[0:n], '.', color='blue', markersize=3)  # Ground Truth
plt.plot(X1[n:m], X2[n:m], '.', color='red', markersize=3)  # Ground Truth
plt.plot(c1_x1, c1_x2, 'o', markersize=5, markeredgecolor='blue', markerfacecolor='None')
plt.plot(c2_x1, c2_x2, 'o', markersize=5, markeredgecolor='red', markerfacecolor='None')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Circle: Classification')

plt.subplot(133)
plt.plot(E)
plt.xlabel('Iterations')
plt.ylabel('E')
plt.title('Error')
plt.show()

##########################################################
print('THETA.T times X = theta0+theta1(X1)+theta2(X2)')
print('------THETA Values---------')
print('theta0 = ', theta0)
print('theta1 = ', theta1)
print('theta2 = ', theta2)

#########  NEW DATA CLASSIFICATION  ######################
Data1 = np.loadtxt(fname='Test_Data.txt')
X1 = Data1[:, 0]  # Feature-1
X2 = Data1[:, 1]  # Feature-2
Y = Data1[:, 2]  # Classes

n = int(len(X1) / 2)  # Half of the data is in class 1 (50 points) *known fact.
m = 2 * n  # No. of data points in total (50+50)
X0 = np.ones(m)  # 1-D vector having 100 elements with value one
X = np.zeros((3, m))  # 3 x 100 matrix with zeros as the elements
X[0] = X0
X[1] = X1
X[2] = X2

H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))
H = H.ravel()  # converting to [] form
H = np.round(H)

c1_x1 = []
c1_x2 = []
c2_x1 = []
c2_x2 = []
for i in range(0, m):
    temp_x1 = X1[i]
    temp_x2 = X2[i]
    val = H[i]
    if val == 0:
        c1_x1.append(temp_x1)
        c1_x2.append(temp_x2)
    else:
        c2_x1.append(temp_x1)
        c2_x2.append(temp_x2)

plt.figure()
plt.subplot(121)
plt.plot(X1[0:n], X2[0:n], '.', color='blue', markersize=3)
plt.plot(X1[n:m], X2[n:m], '.', color='red', markersize=3)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Test Data')
plt.subplot(122)
plt.plot(X1[0:n], X2[0:n], '.', color='blue', markersize=3)  # Ground Truth
plt.plot(X1[n:m], X2[n:m], '.', color='red', markersize=3)  # Ground Truth

plt.plot(c1_x1, c1_x2, 'o', markersize=5, markeredgecolor='blue', markerfacecolor='None')
plt.plot(c2_x1, c2_x2, 'o', markersize=5, markeredgecolor='red', markerfacecolor='None')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Circle: Classification')
plt.show()