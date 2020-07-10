# scientific computing library in python
import numpy as np
# plotting and plot styling
import matplotlib.pyplot as plt
# statistical data visualization
import seaborn as sns
# manage and store data for our function
import pandas as pd

plt.style.use("ggplot")
# %matplotlib inline

from pylab import rcParams

rcParams['figure.figsize'] = 12, 8

# data and objectives of this project
# driver tests written and practical test both must be passed
data = pd.read_csv("DMV_Written_Tests.csv")
data.head()
print(data.head())

# So what we gonna do is learn from above data and predict the results in any given test course
print(data.info())

scores = data[['DMV_Test_1', 'DMV_Test_2']].values
results = data['Results'].values

# visulize data
passed = (results == 1).reshape(100, 1)
failed = (results == 0).reshape(100, 1)

ax = sns.scatterplot(x=scores[passed[:, 0], 0],
                     y=scores[passed[:, 0], 1],
                     marker="^",
                     color='green',
                     s=60)
sns.scatterplot(x=scores[failed[:, 0], 0],
                y=scores[failed[:, 0], 1],
                marker="X",
                color='red',
                s=60)

ax.set(xlabel="DMV Written Test 1 Scores", ylabel="DMV Written Test 2 Sores")
ax.legend(['Passed', 'Failed'])
plt.show()


# define the logistic sigmoid function
def logistic_function(x):
    return 1 / (1 + np.exp(-x))


print(logistic_function(0))


# compute the cost function and gradient
# x-input
# y- class label
# m- number of samples

def compute_cost(theta, x, y):
    m = len(y)
    y_pred = logistic_function(np.dot(x, theta))
    error = (y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    cost = -1 / m * sum(error)
    gradient = 1 / m * np.dot(x.transpose(), (y_pred - y))
    return cost[0], gradient


# compute cost and gradient at initialization
mean_scores = np.mean(scores, axis=0)
# std-standard deviation
std_scores = np.std(scores, axis=0)
scores = (scores - mean_scores) / std_scores

# featurs -x , tatget -y
rows = scores.shape[0]
cols = scores.shape[1]

# feature matrix
X = np.append(np.ones((rows, 1)), scores, axis=1)
y = results.reshape(rows, 1)

theta_init = np.zeros((cols + 1, 1))
cost, gradient = compute_cost(theta_init, X, y)

# cost without any optimization
print("Cost at initialization", cost)
print("Gradients at initializations", gradient)


# gradient descent
def gradient_descent(x, y, theta, alpha, iterations):
    costs = []
    for i in range(iterations):
        cost, gradient = compute_cost(theta, x, y)
        theta -= (alpha * gradient)
        costs.append(cost)
    return theta, costs


theta, costs = gradient_descent(X, y, theta_init, 1, 200)
print("Theta after running gradient descent: ", theta)
print("Resulting cost:", costs[-1])

# plotting the covergence of J
plt.plot(costs)
plt.xlabel("Iterations")
plt.ylabel("$J(\Theta)$")
plt.title("Values of Cost Function over Iterations of Gradient Descent")
plt.show()

# plotting the decision boundary
ax = sns.scatterplot(x=X[passed[:, 0], 1],
                     y=X[passed[:, 0], 2],
                     marker="^",
                     color='green',
                     s=60)
sns.scatterplot(x=X[failed[:, 0], 1],
                y=X[failed[:, 0], 2],
                marker="X",
                color='red',
                s=60)
ax.legend(['passed', 'Failed'])
ax.set(xlabel="DMV Written Test 1 Scores", ylabel="DMV Written Test 2 Scores")

x_boundary = np.array([np.min(X[:, 1]), np.max(X[:, 1])])
y_boundary = -(theta[0] + theta[1] * x_boundary / theta[2])

sns.lineplot(x=x_boundary, y=y_boundary, color="blue")
plt.show()

def predict(theta, x):
    results = x.dot(theta)
    return results>0

p=predict(theta, X)
print("Training Accuracy:", sum(p==y)[0],"%")

test = np.array([50, 79])
test = (test - mean_scores)/std_scores
test = np.append(np.ones(1), test)
probability = logistic_function(test.dot(theta))
print("A person who scores 50 and 79 on their DMV written tests have a",
      np.round(probability[0], 2),"probability of passing")