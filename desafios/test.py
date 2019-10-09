import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import preprocessing

df = pd.read_csv("boston.csv")
df = df.drop(columns='Unnamed: 0')

X = df.drop(['medv'], axis=1)  # features
y = df['medv']  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

X_train_scaled = preprocessing.scale(X_train)
y_train_scaled = preprocessing.scale(y_train)
X_test_scaled = preprocessing.scale(X_test)
y_test_scaled = preprocessing.scale(y_test)

linear_model = LinearRegression()
lfit_unnormed = linear_model.fit(X_train, y_train)
lfit_normed = linear_model.fit(X_train_scaled, y_train_scaled)
#lfit_unnormed = LinearRegression().fit(X_train, y_train)
#lfit_normed = LinearRegression().fit(X_train_scaled, y_train_scaled)

# model evaluation for training and testing sets, normalized and unnormalized
y_train_predict_u = lfit_unnormed.predict(X_train)
y_test_predict_u = lfit_unnormed.predict(X_test)
y_train_predict_n = lfit_normed.predict(X_train_scaled)
y_test_predict_n = lfit_normed.predict(X_test_scaled)


def report_scores(true, predicted):
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2 = r2_score(true, predicted)
    print(f'RMSE is {rmse}')
    print(f'R2 score is {r2}')

report_scores(y_train, y_train_predict_u)
report_scores(y_train_scaled, y_train_predict_n)
