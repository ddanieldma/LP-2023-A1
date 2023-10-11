import sys
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from read import ler_csv
from read import criar_geometria_brasil

def tratar_base() -> GeoDataFrame:
    '''Trata e une as duas bases a fim de utilizá-las para o plot

    :returns: Dataframe pronto para ser utilizado no plot
    :rtype: GeoDataFrame
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
    df_gui_copia.rename({"SG_UF_IES": "sigla"}, axis = 1, inplace = True)

    #Filtragem para se obter a soma de docentes por estado (sigla)
    try:
        df_para_plot = df_gui_copia.groupby("sigla")["QT_DOC_EXE"].sum().reset_index()
    except KeyError:
        print("A coluna especificada não existe (groupby)")
        sys.exit(1)
    
    geometria_brasil = criar_geometria_brasil()

    #Unir as bases da dados com base na columa "sigla"
    try:
        dataframe_plot = geometria_brasil.merge(df_para_plot, on="sigla", how="left")
    except Exception as erro:
        print("O seguinte argumento impossibilitou o merge:", erro)
        sys.exit(1)
    
    return dataframe_plot 
