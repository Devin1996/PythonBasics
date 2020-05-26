# This program is about an example of Logistic Regression with Regularization

import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt(fname='Training_Data.txt')
X1 = Data[:, 0]  # Feature-1
X2 = Data[:, 1]  # Feature-2
Y = Data[:, 2]  # Classes

n = int(len(X1) / 2)  # Half of the data is in class 1 (1000 points) *known fact.
# Other half in class 2.
m = 2 * n  # No. of data points in total  (1000+1000)

X0 = np.ones(m)  # 1-D vector having 2000 elements with value one
X = np.zeros((6, m))  # 6 x 2000 matrix with zeros as the elements
X[0] = X0
X[1] = X1
X[2] = X2
X3 = np.multiply(X1, X1)
X4 = np.multiply(X2, X2)
X5 = np.multiply(X1, X2)
X[3] = X3
X[4] = X4
X[5] = X5

theta0 = 1
theta1 = 1
theta2 = 1
theta3 = 1
theta4 = 1
theta5 = 1
THETA = np.zeros((6, 1))  # 6 x 1 matrix
THETA[0] = theta0
THETA[1] = theta1
THETA[2] = theta2
THETA[3] = theta3
THETA[4] = theta4
THETA[5] = theta5

H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))  # [[ 1 x 2000 ]]
H = H.ravel()  # []  1-D vector
lamb = 1000
COST = (-1 / m) * np.sum(np.multiply(Y, np.log(H)) + np.multiply((1 - Y), np.log(1 - H))) \
       + (lamb / (2 * m)) * np.sum(np.multiply(THETA, THETA))
itr = 1000
E = np.zeros(itr)
THETA_VEC = np.zeros((1, 6))  # 1 x 6 matrix

for i in range(1, itr):  # Appending 999 times
    THETA_VEC = np.append(THETA_VEC, np.zeros((1, 6)), axis=0)

alpha = 0.1
for i in range(0, itr):
    theta0 = theta0 - alpha * (1 / m) * np.sum((np.multiply((H - Y), 1)))
    theta1 = theta1 - alpha * ((1 / m) * np.sum((np.multiply((H - Y), X1))) + (lamb / m) * theta1)
    theta2 = theta2 - alpha * ((1 / m) * np.sum((np.multiply((H - Y), X2))) + (lamb / m) * theta2)
    theta3 = theta3 - alpha * ((1 / m) * np.sum((np.multiply((H - Y), X3))) + (lamb / m) * theta3)
    theta4 = theta4 - alpha * ((1 / m) * np.sum((np.multiply((H - Y), X4))) + (lamb / m) * theta4)
    theta5 = theta5 - alpha * ((1 / m) * np.sum((np.multiply((H - Y), X5))) + (lamb / m) * theta5)
    THETA_VEC[i][0] = theta0
    THETA_VEC[i][1] = theta1
    THETA_VEC[i][2] = theta2
    THETA_VEC[i][3] = theta3
    THETA_VEC[i][4] = theta4
    THETA_VEC[i][5] = theta5
    THETA[0] = theta0
    THETA[1] = theta1
    THETA[2] = theta2
    THETA[3] = theta3
    THETA[4] = theta4
    THETA[5] = theta5
    H = 1 / (1 + np.exp(-1 * np.dot(THETA.T, X)))  # [ [ ] ]
    H = H.ravel()  # converting to  [] form
    COST = (-1 / m) * np.sum(np.multiply(Y, np.log(H)) + np.multiply((1 - Y), np.log(1 - H))) \
           + (lamb / (2 * m)) * np.sum(np.multiply(THETA, THETA))
    E[i] = COST

ind = np.argmin(E)
minV = E[ind]
theta0 = THETA_VEC[ind][0]
theta1 = THETA_VEC[ind][1]
theta2 = THETA_VEC[ind][2]
theta3 = THETA_VEC[ind][3]
theta4 = THETA_VEC[ind][4]
theta5 = THETA_VEC[ind][5]
THETA[0] = theta0
THETA[1] = theta1
THETA[2] = theta2
THETA[3] = theta3
THETA[4] = theta4
THETA[5] = theta5

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
plt.title('Traning Data')

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
print('THETA.T times X = theta0+theta1(X1)+theta2(X2)+theta3(X1^2)+theta4(X2^2)+theta5(X1 x X2)')
print('-----THETA VALUES-----')
print('theta0 = ', theta0)
print('theta1 = ', theta1)
print('theta2 = ', theta2)
print('theta3 = ', theta3)
print('theta4 = ', theta4)
print('theta5 = ', theta5)

#########  NEW DATA CLASSIFICATION  ######################
Data1 = np.loadtxt(fname='Test_Data.txt')
X1 = Data1[:, 0]  # Feature-1
X2 = Data1[:, 1]  # Feature-2
Y = Data1[:, 2]  # Classes

n = int(len(X1) / 2)  # Half of the data is in class 1 (500 points) *known fact.
# Other half in class 2.
m = 2 * n  # No. of data points in total  (500+500)

X0 = np.ones(m)  # 1-D vector having 1000 elements with value one
X = np.zeros((6, m))  # 6 x 1000 matrix with zeros as the elements
X[0] = X0
X[1] = X1
X[2] = X2
X3 = np.multiply(X1, X1)
X4 = np.multiply(X2, X2)
X5 = np.multiply(X1, X2)
X[3] = X3
X[4] = X4
X[5] = X5

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
