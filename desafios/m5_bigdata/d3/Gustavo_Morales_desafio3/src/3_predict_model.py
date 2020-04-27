import pandas as pd
import numpy as np
import pickle
import sys


# best model & data loading
best_model_pkl = 'pkl/best_model.pkl'
test_data_file = 'dat/test_delivery_data.csv'
best_model = pickle.load(open(best_model_pkl, 'rb'))
df_test = pd.read_csv(test_data_file)

# preprocess test-df according to train-df
delay_time_mean = np.mean(df_test['delay_time'])
df_test['delay_time_bin'] = 0
df_test.delay_time_bin = np.where(df_test.delay_time > delay_time_mean, 1, 0)
df_test.drop(columns='delay_time', inplace=True)
cols_obj = df_test.select_dtypes(include='object').columns
df_test = pd.get_dummies(df_test, cols_obj, drop_first=True)

# test dataset definition
obj = 'delay_time_bin'
X_test = df_test.drop([obj], axis=1)
y_test = df_test[obj]

# probabilities (1)
zones = ['II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
for z,p in zip(zones, best_model.predict_proba(X_test)[4:11]):
    print('Zone %s = %.2f' % (z.ljust(4, ' '), p[1]))

# probabilities (2)
stypes = ['Monthly', 'Prepaid', 'Semestral', 'Trimestral', 'Yearly']
for s,p in zip(stypes, best_model.predict_proba(X_test)[11:16]):
    print('Sub. type %s = %.2f' % (s.ljust(10, ' '), p[1]))

# probabilities (3)
menus = ['French', 'Indian', 'Italian', 'Japanese', 'Mexican']
for m,p in zip(menus, best_model.predict_proba(X_test)[4:11]):
    print('Menu %s = %.2f' % (m.ljust(8, ' '), p[1]))
