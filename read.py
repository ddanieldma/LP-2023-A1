import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def ler_csv(caminho_csv):
    return pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')

geometria_brasil = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = "lim_unidade_federacao_a")

geometria_brasil.plot()
plt.show()
