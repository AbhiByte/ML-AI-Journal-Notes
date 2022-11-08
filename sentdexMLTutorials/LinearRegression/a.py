#We begin out journey with regression
#Vid #6
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')

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


X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:] #last 1% of the data

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

#clf = svm.SVR(kernel='poly')
clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)


forecast_set = clf.predict(X_lately) #predicting on the last 1% of the data
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

#Following is just a bunch of wizardry to extract date/time
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
print(df.tail())

#Plotting
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()



