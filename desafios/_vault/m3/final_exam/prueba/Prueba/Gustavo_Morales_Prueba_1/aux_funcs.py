import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC,NuSVC
from sklearn.tree import DecisionTreeClassifier,ExtraTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, mean_squared_error, roc_curve, roc_auc_score
import seaborn as sns

def binarize_object(dataframe):
    """
    dataframe: df
    return: df con atributos object binarizado
    """
    col_del = []
    for i, col in enumerate(dataframe):
        if dataframe[col].dtype == "object":
            dataframe = pd.concat([dataframe, pd.get_dummies(dataframe[col],
                                               drop_first = True,
                                               prefix = col)],
                                   axis = 1)
            col_del.append(col)

    dataframe = dataframe.drop(columns = col_del)
    return dataframe

def plot_describe_variables(dataframe, rows, cols):
    """
    dataframe: df
    rows: filas a graficar
    cols: columnas a graficar

    Se presenta la distribucion de los atributos ya sean tipo object o continuos
    """
    # plt.rcParams['figure.figsize'] = 25, 20
    for index, (colname, serie) in enumerate(dataframe.iteritems()):
        plt.subplot(rows, cols, index + 1)
        if serie.dtype == 'object':
            sns.countplot(serie)
            plt.axhline(serie.value_counts().mean())
            plt.title(colname)
        else:
            sns.distplot(serie)
            plt.axvline(np.mean(serie))
            plt.title(colname)
    plt.tight_layout()

def plot_roc_curve(model, y_test, X_test):
    """
    funcion que grafica curva roc
    model: modelo fiteado
    y_test: y_test
    X_test: X_test
    """
    yhat_pr = model.predict_proba(X_test)[:, 1]
    false_positive, true_positive, threshold = roc_curve(y_test, yhat_pr)
    plt.plot(false_positive, true_positive, lw = 1)
    plt.plot([0, 1], linestyle = "--", lw = 1, color = "tomato")
    plt.ylabel("Verdaderos positivos")
    plt.xlabel("Falsos positivos")
    plt.title("Curva ROC")

    print("AUC: ",roc_auc_score(y_test,yhat_pr))

def prob_to_a_class(model, X_test, clase):
    """
    funcion que genera un dataframe con la clase que se desea y la respectiva
    probabilidad de ocurrencia de la prediccion.
    model: modelo entrenado
    X_test: X_test
    clase: string -> clase que se desea en el dataframe
    """
    pred_proba_test = model.best_estimator_.predict_proba(X_test)
    predicted_proba = X_test.filter(regex = clase, axis = 1)
    predicted_proba['pr_1'] = [i[1] for i in pred_proba_test]

    return predicted_proba

def plot_roc_curve(model, y_test, X_test, model_name):
    """
    funcion que grafica curva roc
    model: modelo fiteado
    y_test: vector objetivo
    X_test: matriz de atributos
    """
    yhat_pr = model.predict_proba(X_test)[:, 1]
    false_positive, true_positive, threshold = roc_curve(y_test, yhat_pr)
    auc_roc = roc_auc_score(y_test, yhat_pr)
    plt.plot(false_positive, true_positive, lw=1, label="AUC = %0.2f" % auc_roc)
    plt.plot([0, 1], linestyle="--", lw=1, color="tomato")
    plt.ylabel("TPR")
    plt.xlabel("FPR")
    plt.title(model_name)
    plt.legend(loc="lower right")

