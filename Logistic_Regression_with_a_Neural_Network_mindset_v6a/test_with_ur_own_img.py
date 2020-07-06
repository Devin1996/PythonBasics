## START CODE HERE ## (PUT YOUR IMAGE NAME)
import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

from Logistic_Regression_with_a_Neural_Network_mindset_v6a.model_that_merge_all_functions import d
from Logistic_Regression_with_a_Neural_Network_mindset_v6a.overview_of_the_problem_set import num_px, classes
from Logistic_Regression_with_a_Neural_Network_mindset_v6a.predict import predict

my_image = "my_image.jpg"   # change this to the name of your image file
## END CODE HERE ##

# We preprocess the image to fit your algorithm.
fname = "images/" + my_image
image = np.array(ndimage.imread(fname, flatten=False))
image = image/255.
my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T
my_predicted_image = predict(d["w"], d["b"], my_image)

plt.imshow(image)
print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")