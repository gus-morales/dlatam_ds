import pandas as pd
import numpy as np
import pickle
import sys
import aux_funcs as af


# best model & data loading
best_model_pkl = 'pkl/best_model.pkl'
valid_data_file = 'dat/valid_delivery_data.csv'
best_model = pickle.load(open(best_model_pkl, 'rb'))
df_valid = pd.read_csv(valid_data_file)

# preprocess valid-df according to train-df
obj = 'delay_time_bin'
df_valid_process = af.preprocess_dataframe(df_valid)
df_valid_process = df_valid_process.drop([obj], axis=1)
df_valid['predict'] = best_model.predict(df_valid_process)

print(df_valid.groupby('delivery_zone')['predict'].mean().sort_values().sort_index().to_string())
print('')
print(df_valid.groupby('deliverer_id')['predict'].mean().sort_values().sort_index().to_string())
print('')
print(df_valid.groupby('menu')['predict'].mean().sort_values().sort_index().to_string())
print('')
print(df_valid.groupby('subscription_type')['predict'].mean().sort_values().sort_index().to_string())
