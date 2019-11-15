def transformaciones(df):
    """For a given dataframe, binarize rows 0-1 (2 category).
    
    Parameters
    ----------
    dataframe : df
        dataframe to transform
    
    Returns
    -------
    print : 'done'
        when ends
    """
    import numpy as np

    columnas = df.columns.to_list()
    for columna in columnas:
        if df[columna].dtypes == 'object':
            valores = df[columna].value_counts().index.tolist()
            valores.pop(0)
            for valor in valores:
                df["bin_"+columna+"_"+valor] = np.where(df[columna] == valor, 1, 0)
    print('done')