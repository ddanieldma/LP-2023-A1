import pandas as pd
import geopandas as gpd
from pandas import DataFrame
from geopandas import GeoDataFrame

def ler_csv(caminho_csv) -> DataFrame: 
    """Recebe um arquivo csv e retona um dataframe

    :param str caminho_csv: caminho do arquivo csv

    :return: DataFrame produzido com base no arquivo csv
    :rtype: pandas.DataFrame
    """
    try:
        df = pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("O caminho deve ser uma string")
    else:
        return df    
    

base_inep = ler_csv("ed-superior-inep.csv")


def criar_geometria_brasil() -> GeoDataFrame:
    """Recebe um arquivo e retona um geodataframe

    :param str caminho_csv: caminho do arquivo (nesse caso, .gpkg)

    :return: GeoDataFrame produzido com base no arquivo
    :rtype: geopandas.GeoDataFrame
    """

    try:
        geometria_brasil = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = "lim_unidade_federacao_a")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("O caminho deve ser uma string")
    else:
        return geometria_brasil
