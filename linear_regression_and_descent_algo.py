# This program is about fitting the line of best fit given data by calculating theta0, theta1 using the analytic expressions
# and comparing the estimated values using Gradient Descent Algorithm

import numpy as np
import matplotlib.pyplot as plt

Y = np.array([100, 140, 210, 220, 290, 270, 300])
X = np.array([450, 650, 675, 850, 950, 1250, 1450])
X = X * (1 / np.max(X))
Y = Y * (1 / np.max(Y))

# print('Shape of X =', X.shape)
X1 = X.copy()  # Needed for later culculations

plt.figure()
plt.subplot(131)
plt.scatter(X, Y, color='red', marker='o', label='Y vs X')
plt.title('Y vs. X')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')

n = len(X)
xbar = np.sum(X) / n
ybar = np.sum(Y) / n

theta1 = np.divide(((np.dot(X, Y) - n * xbar * ybar)), ((np.dot(X, X) - n * np.power(xbar, 2))))
theta0 = ybar - theta1 * xbar

Y_est = theta0 + theta1 * X
print("Theoritical Values")
print("------------------")
print("Theta0=", theta0)
print("Theta1=", theta1)
plt.plot(X, Y_est, color='green')  # Line of best fit in green

theta0 = 1
theta1 = 1
THETA = np.array([theta0, theta1])
THETA = THETA.reshape(2, 1)  # Now, THETA is a column vector

m = len(X)
X0 = np.ones(m)  # 1D array
X0 = X0.reshape(1, m)  # Row vector (1 x m matrix)
X1 = X1.reshape(1, m)  # Reshaping the X1 to be a row vector
Y = Y.reshape(1, m)  # Reshaping the Y to be a row vector
# print('Shape of X1 =', X1.shape)
# print('Shape of Y =', Y.shape)

# X1=[X0;X1];                    #Matlab Syntax
Xdata = np.append(X0, X1, axis=0)  # axis=0 will place X1 row below X0.
H = np.dot(np.transpose(THETA), Xdata)
Error = (1 / (2 * m)) * np.sum((np.power((H - Y), 2)))

alpha = 0.01
itr = 100000
E = [Error]
THETA0 = [theta0]
THETA1 = [theta1]

for i in range(0, itr):
    theta0 = theta0 - (1 / m) * alpha * np.sum((np.multiply((H - Y), 1)))
    theta1 = theta1 - (1 / m) * alpha * np.sum((np.multiply((H - Y), X1)))
    THETA = np.array([theta0, theta1])
    THETA.shape = (2, 1)  # Forcing the shape of 1D array to a column vector (2 x 1)
    THETA0.append(theta0)
    THETA1.append(theta1)
    H = np.dot(np.transpose(THETA), Xdata)
    E.append((1 / (2 * m)) * np.sum(np.power((H - Y), 2)))
    if (E[i] < 0.001):
        break

ind = np.argmin(E)
minV = E[ind]
theta0 = THETA0[ind]
theta1 = THETA1[ind]

# Result of Gradient Descent
print('Results From Gradient Descent')
print('-----------------------------')
print('Estimated theta0 =', theta0)
print('Estimated theta1 =', theta1)
print('Number of Iterations=', ind)
print('Error=', minV)

Y_new = theta0 + theta1 * X1

X = np.ravel(X)  # Flattening the array or converting back to 1D array for plotting purposes.
Y = np.ravel(Y)  # Flattening the array or converting back to 1D array for plotting purposes.
Y_new = np.ravel(Y_new)  # Flattening the array or converting back to 1D array for plotting purposes.

plt.subplot(132)
plt.scatter(X, Y, color='red', marker='o', label='Y vs X')
plt.title('Line of best fit : Gradient Descent')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.plot(X, Y_new, color='blue')

plt.subplot(133)
plt.plot(E)
plt.title('Error vs. Iterations')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()