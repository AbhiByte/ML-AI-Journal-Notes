"""
K-Means is a clustering algorithm used to group data into 'K' groups or clusters.
Must manually specify 'k'. Often very fast.
"""

from sklearn.cluster import KMeans

k = 5
kmeans = KMeans(n_clusters=k)
X = "sample data"
y_pred = kmeans.fit_predict(X)

"""
Algo is guarunteed to converge, but may converge incorrectly :(
To correct this, employ:
"""
"""
Centroid Init Techniques -> If you already know the approx loc of centroids.
"""
import numpy as np

good_init_centroids = np.array([[-3, 3], [-3, 2], [-3, 1], [-1, 2], [0, 2]])
