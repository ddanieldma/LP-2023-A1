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
    """Renomeia a coluna desejada.

    :param pandas.DataFrame df: DataFrame base.
    :param str nome_antigo: Coluna cujo nome será trocado.
    :param str nome_novo: Novo nome para a coluna.

    :return: DataFrame com essa alteração de nome.
    :rtype: pandas.DataFrame
    
    Exemplo:
    >>> dados = {'RJ': [1, 2, 3], 'SP': [4, 5, 6]}
    >>> df = pd.DataFrame(data)
    >>> df = renomear_coluna(df, 'SP', 'MG')
    >>> df
       RJ MG
    0  1  4
    1  2  5
    2  3  6
    """
    df.rename(columns={nome_antigo: nome_novo}, inplace=True)
    
    return df

def agrupamento_de_dados(df, coluna_base, coluna_valores) -> DataFrame:
    """Realiza o agrupamento especificado.

    :param pandas.DataFrame df: DataFrame base.
    :param str coluna_base: O nome da coluna usada para agrupar os dados.
    :param str coluna_valores: Coluna cujos valores serão somados.

    :return: DataFrame processado.
    :rtype: pandas.DataFrame

    Exemplo:
    >>> dados = {'sigla': ['SP', 'RJ', 'SP', 'RJ'], 'QT_DOC_EXE': [100, 200, 150, 250]}
    >>> df = pd.DataFrame(dados)
    >>> resultado = agrupamento_de_dados(df, 'sigla', 'QT_DOC_EXE')
    >>> resultado
      sigla  QT_DOC_EXE
    0    SP        250
    1    RJ        450
    """
    try:
        df_para_plot = df.groupby(coluna_base)[coluna_valores].sum().reset_index()
    except KeyError:
        raise KeyError("A coluna especificada não existe (groupby)")
    
    return df_para_plot


def merge_bases(df1, df2, coluna) -> GeoDataFrame:
    """Realiza o merge de duas bases com base na coluna especificada.

    :param pandas.DataFrame df1: Primeira base para o merge.
    :param pandas.DataFrame df2: Segunda base para o merge.
    :param str coluna: Coluna que servirá de base para o merge.

    :return: DataFrame criado pela junção do df1 e df2.
    :rtype: geopandas.GeoDataFrame

    Exemplo:
    >>> dados1 = {'ID': [1, 2, 3], 'Estados: ['MG', 'RJ', 'SP']}
    >>> dados2 = {'ID': [1, 2, 3], 'Área': [50000, 10000, 70000]}
    >>> df1 = pd.DataFrame(dados1)
    >>> df2 = pd.DataFrame(dados2)
    >>> resultado = merge_bases(dados1, dados2, 'ID')
    >>> resultado
       ID   Estados  Área
    0   1        MG  50000
    1   2        RJ  10000
    2   3        SP  70000
    """
    try:
        dataframe_plot = df1.merge(df2, on=coluna, how="left")
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
    
    geometria_brasil = criar_geometria_brasil("bcim_2016_21_11_2018.gpkg", "lim_unidade_federacao_a")

    #Unir as bases da dados com base na columa "sigla"
    dataframe_plot = merge_bases(geometria_brasil, df_para_plot, "sigla")
    
    return dataframe_plot 


