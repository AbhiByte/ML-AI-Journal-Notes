import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn import svm


csv_path = '/Users/abhir/Desktop/ML-AI-Journal-Notes/HandsOnMLBook/Regression/datasets/housing/housing.csv'
data = pd.read_csv(csv_path)
print(data.head())

from sklearn.preprocessing import LabelEncoder

# Assuming 'X' is your dataset containing the text-based categorical feature
categorical_column = 'ocean_proximity'
# Create a LabelEncoder instance
encoder = LabelEncoder()
# Apply label encoding to the categorical column
data[categorical_column] = encoder.fit_transform(data[categorical_column])
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')  # Choose strategy: mean, median, most_frequent, constant
data.dropna(axis=0, inplace=True)

y = data['median_house_value']
X = data.drop(columns=['median_house_value'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = svm.SVR(kernel="linear")
model.fit(X_train, y_train)
predictions = model.predict(X_test)

import pickle
with open('model_filename.pkl', 'wb') as file:
    pickle.dump(model, file)

