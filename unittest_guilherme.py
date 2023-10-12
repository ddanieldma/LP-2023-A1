'''Módulo destinado a realização do unittest das funções de tratamento de base
'''

import unittest
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from tratamento_base import *

#criando dataframes para serem utilizados nos testes
dados_teste_1 = {"RJ": [1, 2, 3], "SP": [4, 5, 6]}
df_teste_1 = pd.DataFrame(dados_teste_1)

dados_teste_2 = {"RJ": [1, 2, 3], "MG": [4, 5, 6]}
df_teste_2 = pd.DataFrame(dados_teste_2)

dados_teste_3 = {"BARBACENA": [1, 2, 3], "MG": [4, 5, 6]}
df_teste_3 = pd.DataFrame(dados_teste_3)

dados_teste_4 = {"sigla": ["SP", "RJ", "SP", "RJ"], "QT_DOC_EXE": [100, 200, 150, 250]}
df_teste_4 = pd.DataFrame(dados_teste_4)

dados_teste_4 = {"sigla": ["SP", "RJ", "SP", "RJ"], "QT_DOC_EXE": [100, 200, 150, 250]}
df_teste_4 = pd.DataFrame(dados_teste_4)

dados_teste_5 = {"sigla": ["RJ", "SP"], "QT_DOC_EXE": [450, 250]}
df_teste_5 = pd.DataFrame(dados_teste_5)

class TesteFunções(unittest.TestCase):

    def test_função_renomear(self):
        #Não se espera erro
        base_renomeada = renomear_coluna(df_teste_1, "SP", "MG")
        self.assertTrue(base_renomeada.equals(df_teste_2))

    def test_renomear_coluna_2(self):
        #Erro esperado
        base_renomeada = renomear_coluna(df_teste_1, "SP", "MG")
        self.assertTrue(base_renomeada.equals(df_teste_3))

    def test_agrup_dados(self):
        #Não se espera erro
        base_agrupada = agrupamento_de_dados(df_teste_4, "sigla", "QT_DOC_EXE")
        self.assertTrue(base_agrupada.equals(df_teste_5))

    def test_agrup_dados_2(self):
        #Não se espera erro
        base_agrupada = agrupamento_de_dados(df_teste_4, "sigla", "QT_DOC_EXE")
        self.assertTrue(base_agrupada.equals(df_teste_3))

    

if __name__ == "__main__":
    unittest.main()

