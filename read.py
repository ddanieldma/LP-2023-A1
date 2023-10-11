import pandas as pd
import geopandas as gpd
from pandas import DataFrame
from geopandas import GeoDataFrame

def ler_csv(caminho_csv) -> DataFrame:
    return pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')

def criar_geometria_brasil() -> GeoDataFrame:
    geometria_brasil = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = "lim_unidade_federacao_a")
    return geometria_brasil
