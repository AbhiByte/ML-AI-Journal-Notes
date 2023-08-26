#load mnist data
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)
print(mnist.keys())


#split data
X, y = mnist["data"], mnist["target"]
print(X.shape())
