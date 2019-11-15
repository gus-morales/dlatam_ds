def transformaciones(dataframe, exclude):
    """For a given dataframe, binarize rows 0-1.
    
    Parameters
    ----------
    dataframe : dataframe
        dataframe to transform
    
    Returns
    -------
    print : 'done'
        when ends
    """
    import numpy as np

    columnas = dataframe.columns.to_list()
    borrar=[]
    for columna in columnas:
        if columna not in exclude:
            valores = dataframe[columna].value_counts().index.tolist()
            valores.pop(0)
            for valor in valores:
                dataframe["bin_"+columna+"_"+str(valor)] = np.where(dataframe[columna] == valor, 1, 0)
            borrar.append(columna)
    dataframe=dataframe.drop(borrar, axis=1)
    return dataframe


def modelo_descriptivo(dataframe, excluir, vectorobjetivo):
    """Genera un boxplot para cada variable del df en base a un vector objetivo.
    
    Parameters
    ----------
    dataframe : dataframe
        dataframe to transform

    excluir : array
        array con columnas para dejar fuera del analisis ['VAR1','VAR2','VAR3']

    vectorobjetivo : string
        corresponde a la variable del DF a comparar
    
    Returns
    -------
    print : 'done'
        when ends
    """
    nrocolumnas = int(dataframe.shape[1]/3)
    from matplotlib import rcParams
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.rcParams['figure.figsize'] = 20, 80
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(nrocolumnas, 3)
    fig.subplots_adjust(hspace=.5)
    columnas = dataframe.columns.to_list()
    col = 0
    pos = 0
    for columna in columnas:
        if columna not in excluir:
            ax = sns.boxplot(x=dataframe[columna], y=vectorobjetivo, data=dataframe, ax=axes[col, pos])
            pos+=1
            if pos == 3:
                col+=1
                pos = 0

def coefplot(model, varnames=True, intercept=False, fit_stats=True, figsize=(12, 14)):
    """
    coefplot - Visualize coefficient magnitude and approximate frequentist significance from a model.
    
    @parameters:
        - model: a `statsmodels.formula.api` class generated method, which must be already fitted.
        - varnames: if True, y axis will contain the name of all of the variables included in the model. Default: True
        - intercept: if True, coefplot will include the $\beta_{0}$ estimate. Default: False.
        - fit_stats: if True, coefplot will include goodness-of-fit statistics. Default: True.
        
    @returns:
        - A `matplotlib` object.
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    if intercept is True:
        coefs = model.params.values
        errors = model.bse
        if varnames is True:
            varnames = model.params.index
    else:
        coefs = model.params.values[1:]
        errors = model.bse[1:]
        if varnames is True:
            varnames = model.params.index[1:]
            
    tmp_coefs_df = pd.DataFrame({'varnames': varnames, 'coefs': coefs,'error_bars': errors})
    fig, ax = plt.subplots(figsize=figsize)
    ax.errorbar(y=tmp_coefs_df['varnames'], x=tmp_coefs_df['coefs'], 
                xerr=tmp_coefs_df['error_bars'], fmt='o', 
                color='slategray', label='Estimated point')
    ax.axvline(0, color='tomato', linestyle='--', label='Null Effect')
    ax.set_xlabel(r'$\hat{\beta}$')
    fig.tight_layout()
    plt.legend(loc='best')
    
    if fit_stats is True:
        if 'linear_model' in model.__module__.split('.'):
            plt.title(r'R$^{2}$' + "={0}, f-value={1}, n={2}".format(round(model.rsquared, 2),
                                                                     round(model.f_pvalue, 3),
                                                                     model.nobs))
        elif 'discrete_model' in model.__module__.split('.'):
            plt.title("Loglikelihood = {0}, p(ll-Rest)={1}, n={2}".format(round(model.llf, 2),
                                                                          round(model.llr_pvalue, 3),
                                                                          model.nobs))


def quest_batery(dataframe, variable):
    import pandas as pd
    df_letter = dataframe.filter(regex = variable)
    variable, mean = [], []

    for colname, serie in df_letter.iteritems():
        variable.append(colname)
        mean.append(serie.mean())

    tmp_df = pd.DataFrame({"var": variable, "mean": mean}).sort_values(by=["mean"])
    return tmp_df