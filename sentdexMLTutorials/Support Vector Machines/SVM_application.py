#Larger the dataset, slower KNN runs
import numpy as np
from sklearn import preprocessing, neighbors, model_selection, svm
import pandas as pd
accuracies = []

df = pd.read_csv('Classification/breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(columns='id', inplace=True)

X = np.array(df.drop(columns='class')) #features
y = np.array(df['class'])           #labels


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)
