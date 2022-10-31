#We begin out journey with regression
#Vid #3
import pandas as pd
import quandl

df = quandl.get('WIKI/TSLA')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

#Making some changes to the data
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close','HL_PCT','PCT_CHANGE','Adj. Volume']]
print(df.head())