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
        return "Arquivo não encontrado"
    except ValueError:
        return "O caminho deve ser uma string"
    else:
        return df    
    

base_inep = ler_csv("ed-superior-inep.csv")


def criar_geometria_brasil(caminho_arq, layer_arq) -> GeoDataFrame:
    """Recebe um arquivo e retona um geodataframe

    :param str caminho_csv: caminho do arquivo .gpkg

    :return: GeoDataFrame produzido com base no arquivo
    :rtype: geopandas.GeoDataFrame
    """
    try:
        geometria_brasil = gpd.read_file(caminho_arq, layer = layer_arq)
    except ValueError:
        return "O arquivo e/ou a coluna layer não existe/existem"
    except TypeError:
        return "ambos os valores devem ser strings"

    return geometria_brasil

