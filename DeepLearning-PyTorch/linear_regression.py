# 1) Design model (input, output size, forward pass)
# 2) Construct loss and optimizer
# 3) Training loop
#    - forward pass: compute prediction and loss
#    - backward pass: gradients
#    - update weights

import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

# 0) Prepare data
X_numpy, y_numpy =datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)

# 1) Model

# 2) Loss and optimizer

# 3) Training loop