import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, roc_curve, roc_auc_score, confusion_matrix
from IPython.display import display_html

def recod_row(row, original, to, labels):
    """For a given dataframe row, creates a new column based on a label list.
    
    Parameters
    ----------
    row : str
        The dataframe row to be based upon
    original:
	Original label
    to:
        New label
    labels: lst
        List containing all labels
    
    Returns
    -------
    : str
        Corresponding output label
    """
    return to if row[original] in labels else np.nan

def get_scores(cm_object):
    """Given a confusion matrix object, returns performance metrics explicitely.
    
    Parameters
    ----------
    cm_object : object
        The input confusion matrix
    
    Returns
    -------
    : dict
        Dictionary with output metrics
    """
    tn, fp, fn, tp = cm_object.ravel()
    precision = tp / (tp + fp)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    neg_pred_value = tn / (tn + fn)
    f1 = 2*(precision * sensitivity)/(precision + sensitivity)
    return {'precision': precision,
            'accuracy': accuracy,
            'sensitivity (recall)': sensitivity,
            'specificity': specificity,
            'neg_pred_value': neg_pred_value,
            'f1': f1}

def get_confusion_matrix(y, y_pred):
    """Returns a dataframe with the confusion matrix.
    
    Parameters
    ----------
    y : pandas.Series
	target vector
    y_pred : pandas.Series
    	predicted target vector
    
    Returns
    -------
    : pandas.DataFrame
	Table with the confusion matrix values
    """
    cm = confusion_matrix(y, y_pred)
    tn, fp, fn, tp = cm.ravel()
    df1 = pd.DataFrame.from_dict({'predicted positive': f'TP = {tp}', 'predicted negative': f'FN = {fn} (type II)'},
                                 orient='index', columns=['actual positive'])
    df2 = pd.DataFrame.from_dict({'predicted positive': f'FP = {fp} (type I)', 'predicted negative': f'TN = {tn}'},
                                 orient='index', columns=['actual negative'])
    return pd.concat([df1,df2], axis=1)

def get_model_evaluation_report(y, y_pred_log, y_pred_probs_log, title):
    """Prints classification report, AUC score and ROC curve for a given fitted model.

    Parameters
    ----------
    y : pandas.Series
	target vector
    y_pred_log : pandas.Series
    	predicted target vector
    y_pred_probs_log : pandas.Series
    	probabilities for the predicted target vector 
    """
    print(title)
    print(classification_report(y, y_pred_log))
    auc = roc_auc_score(y, y_pred_probs_log)
    fpr, tpr, thresholds = roc_curve(y, y_pred_probs_log)
    plt.rcParams['figure.figsize'] = 6, 4
    plt.plot(fpr, tpr, label=f'ROC curve: AUC={auc:0.2f}')
    plt.xlabel('1 - Specificity (false positive rate)')
    plt.ylabel('Sensitivity (true positive rate)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

def binarize(dataframe):
    """Binarizes dataframe columns, generating one new column for each label.
    
    Parameters
    ----------
    dataframe : pandas.DataFrame
	DataFrame object with input data

    Returns
    -------
    cols : array
	Altered DataFrame columns
    """
    cols = []
    for col in dataframe.columns.to_list():
        if dataframe[col].dtypes == 'object':
            values = dataframe[col].value_counts().index.tolist()
            values.pop(0)
            for val in values:
                dataframe["bin_"+col+"_"+val] = np.where(dataframe[col] == val, 1, 0)
            cols.append(col)
    return cols

def binarize_binary(dataframe):
    """Binarizes dataframe binary columns.
    
    Parameters
    ----------
    dataframe : pandas.DataFrame
	DataFrame object with input data
    """
    for col in dataframe.columns.tolist():
        index = dataframe[col].value_counts().index
        if len(dataframe[col].value_counts()) == 2:
            dataframe[col] = np.where(dataframe[col]==index[1], 1, 0)

def generate_formula(variables, dep_variable):
    """Creates a formula_like string, useful for some statmodels methods.
    
    Parameters
    ----------
    variables: list
	List with column names
    dep_variable: string
	Name of the target variable

    Returns
    -------
    formula : string
	formula_like string
    """
    formula = dep_variable + ' ~ '
    for var in variables:
        if var != dep_variable:
            formula += var
            formula += ' + '
    formula = formula[:-3]
    return formula

def display_side_by_side(*args):
    """Displays an arbitrary amount of pandas DataFrames next to each other.

    Parameters
    ----------
    *args: pandas.DataFrame
	DataFrames to be shown
    """
    html_str=''
    for dfr in args:
        html_str += dfr.to_html()
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
