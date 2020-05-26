import numpy as np
import matplotlib.pyplot as plt

Y = np.array([100, 140, 210, 220, 290, 270, 300])
X = np.array([450, 650, 850, 950, 1250, 1450])
X = X * (1 / np.max(X))
Y = Y * (1 / np.max(Y))

# print('Shape of X = ', X.shape)
X1 = X.copy()

plt.figure()
plt.subplot(131)
plt.scatter(X, Y, color='red', marker='o', label='Y vs X')
plt.title('Y vs X')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')

n = len(X)
xbar = np.sum(X) / n
ybar = np.sum(Y) / n

thetal = np.divide((np.dot(X, Y) - n * xbar * ybar), (np.dot(X, X) - n * np.power(xbar, 2)))
theta0 = ybar-thetal*xbar

Y_est = theta0 + thetal * X
print("Theoritical Values")
print("________________")
print("Theta0", theta0)
print("Theta1=", thetal)
plt.plot(X, Y_est, color='green')  #Line of best fit in green

