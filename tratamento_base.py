'''Módulo que trata a base
'''

import sys
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pandas import DataFrame
from geopandas import GeoDataFrame
from read import ler_csv
from read import criar_geometria_brasil

def renomear_coluna(df, nome_antigo, nome_novo) -> DataFrame:
    df.rename(columns={nome_antigo: nome_novo}, inplace=True)
    return df

def agrupamento_de_dados(df, coluna_base, coluna_valores) -> DataFrame:
    try:
        df_para_plot = df.groupby(coluna_base)[coluna_valores].sum().reset_index()
    except KeyError:
        raise KeyError("A coluna especificada não existe (groupby)")
    return df_para_plot

def merge_bases(base1, base2, coluna):
    try:
        dataframe_plot = base1.merge(base2, on=coluna, how="left")
    except Exception as erro:
        print("O seguinte argumento impossibilitou o merge:", erro)
        sys.exit(1)
    
    return dataframe_plot

def tratar_base() -> GeoDataFrame:
    '''Une as funções de tratamento de base para retornar o dataframe final
    '''  

    try:
        df_guilherme = ler_csv("ed-superior-inep.csv")
    except ValueError:
        print("O caminho deve ser uma string (ler_csv)")
        sys.exit(1)
    except FileNotFoundError:
        print("arquivo não encontrado (ler_csv)")
        sys.exit(1)

    df_gui_copia = df_guilherme.copy()

    #Renomear para igualar o nome da colunas nas bases
    renomear_coluna(df_gui_copia, "SG_UF_IES", "sigla")

    #Filtragem para se obter a soma de docentes por estado (sigla)
    df_para_plot = agrupamento_de_dados(df_gui_copia, "sigla", "QT_DOC_EXE")
    
    geometria_brasil = criar_geometria_brasil()

    #Unir as bases da dados com base na columa "sigla"
    dataframe_plot = merge_bases(geometria_brasil, df_para_plot, "sigla")
    
    return dataframe_plot 


