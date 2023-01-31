import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sys
sys.path.insert(0, '/Users/abhir/Desktop/ML-AI-Journal-Notes/sentdexMLTutorials/LinearRegression')
import regression_algo_manual as ram

df = pd.read_csv('./Kaggle/Life Expectancy Data.csv')
print(df.head())

X = df.drop('Life expectancy', axis=1)
df['custom score'] = df['Adult Mortality'] + df['infant deaths']
Y = df['custom score']


