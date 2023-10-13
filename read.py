import pandas as pd
import geopandas as gpd

def ler_csv(caminho_csv): 

    try:
        df = pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("O caminho deve ser uma string")
    else:
        return df    
    

base_inep = ler_csv("ed-superior-inep.csv")


def criar_geometria_brasil():

    try:
        geometria_brasil = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = "lim_unidade_federacao_a")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except ValueError:
        print("O caminho deve ser uma string")
    else:
        return geometria_brasil
