### One reason why we use "numpy" instead of "math" in Deep Learning ###
import numpy as np

x = [1, 2, 3]

x = np.array([1, 2, 3])
print(np.exp(x))

x = np.array([1, 2, 3])
print (x + 3)


def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + np.exp(-x))
    ### END CODE HERE ###

    return s

x = np.array([1, 2, 3])
y= sigmoid(x)
print(y)