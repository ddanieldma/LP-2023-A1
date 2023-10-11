import pandas as pd
import numpy as np
from read import ler_csv

# Lendo csv
df_ens_sup = ler_csv("ed-superior-inep.csv")

# Dropando as colunas com drop
df_ens_sup.drop(["NU_ANO_CENSO", "CO_MUNICIPIO_IES", "CO_UF_IES", "CO_REGIAO_IES"],axis=1, inplace=True)

# Setting the columns that we need
def removing_columns(dataframe, start_col: str, end_col: str):
    beginning_col = dataframe.columns.get_loc(start_col)
    finish_col = dataframe.columns.get_loc(end_col)
    cols_to_drop = dataframe.columns[beginning_col:finish_col+1]
    dataframe.drop(cols_to_drop, axis=1, inplace=True)

removing_columns(df_ens_sup, "NO_MANTENEDORA", "QT_LIVRO_ELETRONICO")
removing_columns(df_ens_sup, "QT_DOC_EX_INT", "NO_LOCAL_OFERTA")
removing_columns(df_ens_sup, "NO_MESORREGIAO_IES", "CO_MICRORREGIAO_IES")

# Adding the difference between public and private school
types_of_universities = {1: "Pública", 2:"Pública", 3: "Pública", 4: "Privada", 5:"Privada", 6:"Privada", 7: "Privada", 8: "Privada", 9: "Privada"}
specific_type = {1 : "Pública Federal", 2: "Pública Estadual", 3: "Pública Municipal", 4: "Privada com fins lucrativos", 5: "Privada sem fins lucrativos", 6: "Privada - Particular em sentido estrito", 7 : "Especial", 8: "Privada comunitária", 9: "Privada confessional"}


print(df_ens_sup)