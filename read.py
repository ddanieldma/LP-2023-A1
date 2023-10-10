import pandas as pd

def ler_csv(caminho_csv):
    return pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')

"""
Adicionar tratamento de exceção
"""

base_inep = ler_csv("ed-superior-inep.csv")

print(base_inep.head())