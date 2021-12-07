import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn import linear_model, svm
from sklearn.metrics import mean_absolute_percentage_error

data = pd.read_excel("applePrice1.xlsx", engine='openpyxl')

print(data.head())
# print(data.info())
# print(data.isnull().sum())

import datetime
from datetime import datetime

dt = data["date"]

# dt = dt.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
data["month"] = dt.map(lambda x: x.month)

print(data)

# encoder = OneHotEncoder(handle_unknown='ignore')
# newdata = encoder.fit_transform(data[['name']])

newdata = pd.get_dummies(data[['name', 'city']])
newdata['month'] = data['month']

print(newdata.head())

X = newdata[:]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

min_max_scaler = MinMaxScaler()
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.fit_transform(X_test)

model = svm.SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)

score = mean_absolute_percentage_error(y_test, y_pred)
print(score)