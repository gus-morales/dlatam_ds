import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report


# data loading
Path("txt/").mkdir(parents=True, exist_ok=True)
Path("pkl/").mkdir(parents=True, exist_ok=True)
train_data_file = 'dat/train_delivery_data.csv'
##test_data_file = 'dat/test_delivery_data.csv'
df_train = pd.read_csv(train_data_file)
##df_test = pd.read_csv(test_data_file)

# train: redefine target vector
delay_time_mean = np.mean(df_train['delay_time'])
df_train['delay_time_bin'] = 0
df_train.delay_time_bin = np.where(df_train.delay_time > delay_time_mean, 1, 0)
df_train.drop(columns='delay_time', inplace=True)

# train: convert categorical variables into dummy variables
cols_obj = df_train.select_dtypes(include='object').columns
df_train = pd.get_dummies(df_train, cols_obj, drop_first=True)

# test: redefine target vector
##delay_time_mean = np.mean(df_test['delay_time'])
##df_test['delay_time_bin'] = 0
##df_test.delay_time_bin = np.where(df_test.delay_time > delay_time_mean, 1, 0)
##df_test.drop(columns='delay_time', inplace=True)

# test: convert categorical variables into dummy variables
##cols_obj = df_test.select_dtypes(include='object').columns
##df_test = pd.get_dummies(df_test, cols_obj, drop_first=True)

# generate train & testing sets
obj = 'delay_time_bin'
X = df_train.drop([obj], axis=1)
y = df_train[obj]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=11238)
##X_train = df_train.drop([obj], axis=1)
##y_train = df_train[obj]
##X_test = df_test.drop([obj], axis=1)
##y_test = df_test[obj]

# model training
lr = LogisticRegression(max_iter=1000).fit(X_train, y_train)
dt = DecisionTreeClassifier().fit(X_train, y_train)
rf = RandomForestClassifier().fit(X_train, y_train)
gb = GradientBoostingClassifier().fit(X_train, y_train)
nb = BernoulliNB().fit(X_train, y_train)

# printing results
print('lr --------------------------------------------------')
print(classification_report(y_test, lr.predict(X_test)))
print('dt --------------------------------------------------')
print(classification_report(y_test, dt.predict(X_test)))
print('rf --------------------------------------------------')
print(classification_report(y_test, rf.predict(X_test)))
print('gb --------------------------------------------------')
print(classification_report(y_test, gb.predict(X_test)))
print('nb --------------------------------------------------')
print(classification_report(y_test, nb.predict(X_test)))

# pickling best model
print("Best model is: (input here)")
inp = input()
options = {'lr': lr, 'dt': dt, 'rf': rf, 'gb': gb, 'nb': nb}
best_model = options[inp]
outfile = 'pkl/best_model.pkl'
pickle.dump(best_model, open(outfile, "wb"))
print("DONE --> %s model saved at %s" % (inp, outfile))
