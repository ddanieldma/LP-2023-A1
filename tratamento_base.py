import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from read import ler_csv
from read import criar_geometria_brasil

def tratar_base() -> GeoDataFrame:
    df_guilherme = ler_csv("ed-superior-inep.csv")
    df_gui_copia = df_guilherme.copy()
    df_gui_copia.rename({"SG_UF_IES": "sigla"}, axis = 1, inplace = True)
    df_para_plot = df_gui_copia.groupby("sigla")["QT_DOC_EXE"].sum().reset_index()

    geometria_brasil = criar_geometria_brasil()

    dataframe_plot = geometria_brasil.merge(df_para_plot, on = "sigla", how = "left")

    return dataframe_plot