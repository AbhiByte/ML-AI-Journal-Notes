from EuclidianGeometry import EuclideanDistance
import numpy as np
import warnings
from math import sqrt
import pandas as pd
import random

from collections import Counter

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

    confidence = Counter(votes).most_common(1)[0][1] / k

    #print(vote_result, confidence)

    return vote_result, confidence

accuracies = []

for i in range(25):
    df = pd.read_csv('Classification/breast-cancer-wisconsin.data')
    df.replace("?", "-99999", inplace=True)
    df.drop("id", 1, inplace=True)
    full_data = df.astype(float).values.tolist()

    random.shuffle(full_data)

    test_size = 0.4
    train_set = {2:[], 4:[]}
    test_set = {2:[], 4:[]}
    train_data = full_data[:-int(test_size * len(full_data))]
    test_data = full_data[-int(test_size * len(full_data)):]

    for i in train_data:
        train_set[i[-1]].append(i[:-1])
    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    correct = 0
    total = 0

    for group in test_set:
        for data in test_set[group]:
            vote, confidence = k_nearest_neighbours(train_set, data, k=5)
            if group == vote:
                correct+=1
            total+=1
    #print('Accuracy: ', correct/total)
    accuracies.append(correct/total)


print(sum(accuracies)/len(accuracies))