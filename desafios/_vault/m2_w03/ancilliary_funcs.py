# ancilliary_funcs.py
import pandas as pd
import matplotlib.pyplot as plt

def get_na(dataframe, var, print_list=False):
    """Returns the quantity and fraction of the 'dataframe' where the input variable 'var' is NaN.
    If asked for, returns the 'dataframe' indices of such cases instead.
    """
    na_df = dataframe[var].isna()

    # here 'ascending' is set to False to not change the output ordering
    na_quantity = na_df.value_counts(ascending=False)
    na_fraction = na_df.value_counts('%', ascending=False)
    if print_list:
        return dataframe[dataframe[var].isna()][var]

    """
    I have no idea how to force value_counts() to not drop an index
    when one boolean frequency is zero, so I will cover all cases.
    I also do not remember how to select by non-integer index, so I had to
    turn off sorting above and select using iloc.
    """
    res_dict = {}
    # if SOME values are NaN
    if len(na_quantity) > 1 and print_list == False:
        res_dict = {'variable': var,
                    'na_quantity': na_quantity.iloc[1],
                    'na_fraction': na_fraction.iloc[1]
        }
    # if everything is NaN
    if len(na_quantity) == 1 and na_df.value_counts().index[0] == True and print_list == False:
        res_dict = {'variable': var,
                    'na_quantity': na_quantity.iloc[0],
                    'na_fraction': na_fraction.iloc[0]
        }
    # if nothing is NaN
    if len(na_quantity) == 1 and na_df.value_counts().index[0] == False and print_list == False:
        res_dict = {'variable': var,
                    'na_quantity': 0,
                    'na_fraction': 0
        }
    return res_dict

def plot_dotplot(dataframe, plot_var, plot_by, global_stat=False, statistic='mean'):
    if statistic == 'mean':
        stat = dataframe.groupby(plot_by)[plot_var].mean()
    if statistic == 'median':
        stat = dataframe.groupby(plot_by)[plot_var].median()
    plt.plot(stat.values, stat.index.tolist(), 'o', label=plot_by)
    if global_stat:
        mean_tot = dataframe[plot_var].dropna().mean()
        plt.axvline(mean_tot, lw=2, color='tomato', ls='--', label='true_mean')
    plt.legend()
    plt.grid(axis='y')
    plt.xlabel(plot_var)
    plt.tight_layout()
