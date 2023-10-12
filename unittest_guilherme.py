'''Módulo destinado a realização do unittest das funções de tratamento de base
'''

import unittest
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from tratamento_base import merge_bases
from tratamento_base import agrupamento_de_dados
from tratamento_base import renomear_coluna

#criando dataframes para serem utilizados nos testes
dados_teste_1 = {"RJ": [1, 2, 3], "SP": [4, 5, 6]}
df_teste_1 = pd.DataFrame(dados_teste_1)

dados_teste_2 = {"RJ": [1, 2, 3], "MG": [4, 5, 6]}
df_teste_2 = pd.DataFrame(dados_teste_2)

dados_teste_3 = {"BARBACENA": [1, 2, 3], "MG": [4, 5, 6]}
df_teste_3 = pd.DataFrame(dados_teste_2)

class TesteFunções(unittest.TestCase):

    def teste_função_renomear(self):
        #Não se espera erro
        base_renomeada = renomear_coluna(df_teste_1, "SP", "MG")
        self.assertTrue(base_renomeada.equals(df_teste_2))

    def test_renomear_coluna_2(self):
        #Erro esperado
        with self.assertRaises(AssertionError):
            base_renomeada = renomear_coluna(df_teste_1, "SP", "MG")
            self.assertTrue(base_renomeada.equals(df_teste_3))

if __name__ == "__main__":
    unittest.main()
