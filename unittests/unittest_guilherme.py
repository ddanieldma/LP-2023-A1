'''Módulo destinado a realização do unittest das funções de tratamento de base
'''
import sys
sys.path.append("../functions/database")
import unittest
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from tratamento_base import *

#criando dataframes para serem utilizados nos testes
dados_teste_renomear_1 = {"RJ": [1, 2, 3], "SP": [4, 5, 6]}
df_teste_renomear_1 = pd.DataFrame(dados_teste_renomear_1)

dados_teste_renomear_2 = {"RJ": [1, 2, 3], "MG": [4, 5, 6]}
df_teste_renomear_2 = pd.DataFrame(dados_teste_renomear_2)

dados_teste_agrupar_1 = {"sigla": ["SP", "RJ", "SP", "RJ"], "QT_DOC_EXE": [100, 200, 150, 250]}
df_teste_agrupar_1 = pd.DataFrame(dados_teste_agrupar_1)

dados_teste_agrupar_2 = {"sigla": ["RJ", "SP"], "QT_DOC_EXE": [450, 250]}
df_teste_agrupar_2 = pd.DataFrame(dados_teste_agrupar_2)

dados_teste_merge_1 = {"ID": [1, 2, 3], "Estados": ["MG", "RJ", "SP"]}
df_teste_merge_1 = pd.DataFrame(dados_teste_merge_1)
dados_teste_merge_2 = {"ID": [1, 2, 3], "Área": [50000, 10000, 70000]}
df_teste_merge_2 = pd.DataFrame(dados_teste_merge_2)
dados_teste_merge_3 = {"ID": [1, 2, 3], "Estados": ["MG", "RJ", "SP"], "Área": [50000, 10000, 70000]}
df_teste_merge_3 = pd.DataFrame(dados_teste_merge_3)

class TesteFunções(unittest.TestCase):

    def test_função_renomear(self):
        #Comparando bases que devem ser iguais
        base_renomeada = renomear_coluna(df_teste_renomear_1, "SP", "MG")
        pd.testing.assert_frame_equal(base_renomeada, df_teste_renomear_2)

    def test_agrup_dados(self):
        #Comparando bases que devem ser iguais
        base_agrupada = agrupamento_de_dados(df_teste_agrupar_1, "sigla", "QT_DOC_EXE")
        pd.testing.assert_frame_equal(base_agrupada, df_teste_agrupar_2)

        #Passando uma coluna que não existe
        output_esperado = "A coluna especificada não existe ou seus valores não podem ser somados"
        self.assertEqual(agrupamento_de_dados(df_teste_agrupar_1, "silas", "QT_DOC_EXE"), output_esperado)

        #Passando uma coluna cujos valores não podem ser somados
        output_esperado = "A coluna especificada não existe ou seus valores não podem ser somados"
        self.assertEqual(agrupamento_de_dados(df_teste_agrupar_1, "QT_DOC_EXE", "siglas"), output_esperado)

    def test_merge_bases(self):
        #Comparando bases que devem ser iguais
        base_resultado = merge_bases(df_teste_merge_1, df_teste_merge_2, "ID")
        pd.testing.assert_frame_equal(base_resultado, df_teste_merge_3)

        #Passando uma coluna que não existe
        output_esperado = "A coluna especificada não existe"
        self.assertEqual(merge_bases(df_teste_merge_1, df_teste_merge_2, "FGV"), output_esperado)

if __name__ == "__main__":
    unittest.main()

