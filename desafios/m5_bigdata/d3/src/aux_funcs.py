import numpy as np
import pandas as pd


def preprocess_dataframe(dataframe):
    # redefine target vector
    delay_time_mean = np.mean(dataframe['delay_time'])
    dataframe['delay_time_bin'] = 0
    dataframe.delay_time_bin = np.where(dataframe.delay_time > delay_time_mean, 1, 0)
    dataframe.drop(columns='delay_time', inplace=True)

    # convert categorical variables into dummy variables
    cols_obj = dataframe.select_dtypes(include='object').columns
    dataframe = pd.get_dummies(dataframe, cols_obj, drop_first=True)

    return dataframe
