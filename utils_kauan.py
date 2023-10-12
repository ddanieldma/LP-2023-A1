import pandas as pd
import numpy as np

### Limpando a base

def removing_list_columns(dataframe, list):
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
    dataframe["TIPO_UNI"] = dataframe[column].map(types_of_universities)
    return dataframe

######################################################################################
# Análise
def agrupando_por_soma(dataframe, arg1, arg2):
    dataframe = dataframe.groupby(by=[arg1, arg2]).sum()
    return dataframe

def cria_porcentagem(dataframe, nome_col, num_doc_esp, total_por_UF):
    dataframe[nome_col] = dataframe[num_doc_esp]/total_por_UF
    return dataframe


