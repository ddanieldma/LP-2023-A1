import pandas as pd
import numpy as np
import matplotlib.ticker as mtick

def removing_list_columns(dataframe: pd.DataFrame, list: list) -> pd.DataFrame:
    """
    
    """
    dataframe.drop(list, axis=1, inplace=True)
    return dataframe

# Setting the columns that we need
def removing_columns_from_to(dataframe, start_col: str, end_col: str):
    beginning_col = dataframe.columns.get_loc(start_col)
    finish_col = dataframe.columns.get_loc(end_col)
    cols_to_drop = dataframe.columns[beginning_col:finish_col+1]
    dataframe.drop(cols_to_drop, axis=1, inplace=True)
    return dataframe

# Dizendo se é pública ou privada
def type_of_university(dataframe, column = "TP_CATEGORIA_ADMINISTRATIVA"):
    types_of_universities = {1: "Pública", 2:"Pública", 3: "Pública", 4: "Privada", 5:"Privada", 6:"Privada", 7: "Privada", 8: "Privada", 9: "Privada"}
    dataframe["Tipo de Universidade"] = dataframe[column].map(types_of_universities)
    return dataframe

######################################################################################
# Análise
def agrupando_por_soma(dataframe, arg1, arg2):
    dataframe = dataframe.groupby(by=[arg1, arg2]).sum()
    return dataframe

def cria_porcentagem(dataframe, nome_col, num_doc_esp, total_por_UF):
    dataframe[nome_col] = (dataframe[num_doc_esp]/total_por_UF)*100
    return dataframe

def cria_base_ordem_crescente(dataframe, index_to_unstack ,col_porcentagem):

    dataframe = dataframe.unstack(index_to_unstack)[col_porcentagem]
    sum_percentage = dataframe.sum(axis=1)
    dataframe = dataframe.loc[sum_percentage.sort_values(ascending=True).index]
    return dataframe

#####################################################################
# making each plot
def formata_cada_plot(dataframe, title, numberplot, axis):
    dataframe.plot(kind="bar", stacked=True, ax=axis[numberplot])
    axis[numberplot].set_title(title)
    axis[numberplot].yaxis.set_major_formatter(mtick.PercentFormatter())
    axis[numberplot].set_ylim(0, 60)
    axis[numberplot].tick_params(axis='x', rotation=0, labelsize = 7)
    axis[numberplot].set_xlabel("Unidade Federativa")
    axis[numberplot].set_ylabel("Porcentagem")

