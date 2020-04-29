import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import aux_funcs as af


# data loading & preprocess
Path("txt/").mkdir(parents=True, exist_ok=True)
Path("pkl/").mkdir(parents=True, exist_ok=True)
train_data_file = 'dat/train_delivery_data.csv'
df_train = pd.read_csv(train_data_file)
df_train = af.preprocess_dataframe(df_train)

# generate train & testing sets
obj = 'delay_time_bin'
X = df_train.drop([obj], axis=1)
y = df_train[obj]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=11238)

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
