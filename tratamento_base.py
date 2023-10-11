import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from read import ler_csv
from read import criar_geometria_brasil
import pyproj

def tratar_base() -> GeoDataFrame:
    '''Trata e une as duas bases a fim de utilizá-las para o plot

    :returns: Dataframe pronto para ser utilizado no plot
    :rtype: GeoDataFrame
    '''  

    df_guilherme = ler_csv("ed-superior-inep.csv")
    df_gui_copia = df_guilherme.copy()

    #Renomar para igualar o nome da colunas nas bases
    df_gui_copia.rename({"SG_UF_IES": "sigla"}, axis = 1, inplace = True)

    df_para_plot = df_gui_copia.groupby("sigla")["QT_DOC_EXE"].sum().reset_index()

    geometria_brasil = criar_geometria_brasil()

    #Unir as bases da dados com base na columa "sigla"
    dataframe_plot = geometria_brasil.merge(df_para_plot, on = "sigla", how = "left")

    return dataframe_plot

geometria_brasil = criar_geometria_brasil()
print(geometria_brasil.crs)