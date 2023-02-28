#Larger the dataset, slower KNN runs
import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd
accuracies = []
for i in range(25):
    df = pd.read_csv('Classification/breast-cancer-wisconsin.data')
    df.replace('?', -99999, inplace=True)
    df.drop(columns='id', inplace=True)

    X = np.array(df.drop(columns='class')) #features
    y = np.array(df['class'])           #labels


    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=1)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)

    #print(accuracy)

    example_measures = np.array([[2, 2, 1, 1, 1, 2, 3, 2, 1], [10, 8, 7, 8, 9, 4, 7, 8, 9]])
    example_measures = example_measures.reshape(len(example_measures), -1)

    prediction = clf.predict(example_measures)
    #print(prediction)
    accuracies.append(accuracy)
print(sum(accuracies)/len(accuracies))


