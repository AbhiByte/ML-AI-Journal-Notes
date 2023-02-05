from EuclidianGeometry import EuclideanDistance
import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

# dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
# new_feautures = [5, 7]



def k_nearest_neighbours(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a val less than total voting groups!')
    distances = []
    for group in data:
        for feautures in data[group]:
            #euclidean_distance = EuclideanDistance(feautures, predict)
            euclidean_distance = np.linalg.norm(np.array(feautures) - np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result


result = k_nearest_neighbours(dataset, new_feautures, k=3)
print(f"class: {result}")


[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]]for i in dataset]
plt.scatter(new_feautures[0], new_feautures[1], color=result, s=100)
plt.show()