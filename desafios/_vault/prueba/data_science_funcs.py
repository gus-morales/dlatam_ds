import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

def to_string(df, val):
    """
    Parametros: dataframe, nombre de la columna
    Función que convierte valores con comillas a string sin comillas
    """
    df[val].replace(regex = True, inplace = True, to_replace = r"\D", value = r"")

def to_integer(df, cols):
    """
    Función que parsea el tipo de dato de una a columna a tipo entero.
    Parametros:
    dataframe: set de datos
    cols: lista con el nombre de columnas a convertir
    """
    for col in cols:
        df[col] = pd.to_numeric(df[col])

def binarize_cols(df):
    """
    Parametros: dataframe
    Función global que al ser invocada considera todas las columnas del set de datos,
    si la columna presenta solo 2 categorias esta es binarizada.
    """
    col_list = df.columns.tolist()

    for col in col_list:
        index = df[col].value_counts().index
        if len(df[col].value_counts()) == 2:
            print(df[col].value_counts())
            df[col] = np.where(df[col] == index[1], 1, 0)

def bin_nom(df, column):
    """
    Parametros:
    Dataframe
    Column -> columna nominal
    Función que binariza una columna nominal (mas de 2 categorias) según la cantidad de
    categorias y genera nuevas columnas en el dataframe.
    """
    bin_col = df[column].value_counts().index.tolist()
    bin_col.pop(0)

    for col in bin_col:
        df["bin_"+column+"_"+col] = np.where(df[column] == col, 1, 0)

def obj_boxplot(vary, dataframe):
    """
    Parametros:
    vary -> vector objetivo como eje y
    dataframe -> set de datos

    Función que realiza un gráfico de cajas según valores ingresados.
    """
    cols = dataframe.columns
    for col in cols:
        if col != vary:
            sns.boxplot(x = col, y = vary, data = dataframe)
        plt.show()
