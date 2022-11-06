#We begin out journey with regression
#Vid #5
import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/TSLA')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

#Making some changes to the data
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close','HL_PCT','PCT_CHANGE','Adj. Volume']]

#Feature
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

#Predicting out 1% of the length of the data
forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

#Shifting the labels up 1% since we are predicting 10% into the future
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

#clf = svm.SVR(kernel='poly')
clf = LinearRegression()
clf.fit(X_train, y_train)
accurancy = clf.score(X_test, y_test)

print(accurancy)


