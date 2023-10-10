import pandas as pd
import geopandas as gpd

def ler_csv(caminho_csv):
    return pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')

"""
Adicionar tratamento de exceção
"""

base_inep = ler_csv("ed-superior-inep.csv")

def criar_geometria_brasil():
    geometria_brasil = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = "lim_unidade_federacao_a")
    return geometria_brasil
