''' Módulo destinado a realizar os unittest das funções de leitura de arquivos
'''

import unittest
import geopandas as gpd
import pandas as pd
from read import *

class TesteFunçõesMain(unittest.TestCase):

    def test_função_read1(self):
        #Não se espera falha (dataframes iguais)

        dados1 = {"estado":["MG", "SP", "RJ"], "DDD":[32, 11, 21]}
        df_teste_1 = pd.DataFrame(dados1)

        true_df = ler_csv("csv1_unittest.csv")

        pd.testing.assert_frame_equal(true_df, df_teste_1)

    def test_função_read2(self):
        #Se espera falha (dataframes diferentes)

        dados2 = {"estado":["MG", "SP", "Malibu"], "DDD":[200, 11, 21]}
        df_teste_2 = pd.DataFrame(dados2)

        true_df = ler_csv("csv1_unittest.csv")

        pd.testing.assert_frame_equal(true_df, df_teste_2)

    def test_função_read3(self):
        #Se espera falha (FileNotFoundError está tratado)
        
        with self.assertRaises(FileNotFoundError):
            ler_csv("fgv_emap.csv")

    def test_função_read4(self):
        #Se espera falha (ValueError está tratado)  

        with self.assertRaises(ValueError):
            ler_csv(10)
    
    def test_função_geom_br1(self):
        #Não se espera falha (resultado deve ser um GeoDataFrame)

        geodf = criar_geometria_brasil("bcim_2016_21_11_2018.gpkg", "lim_unidade_federacao_a")
        
        self.assertIsInstance(geodf, gpd.GeoDataFrame)

    def test_função_geom_br2(self):
        #Se espera falha (FileNotFoundError está tratado)
        
        with self.assertRaises(Exception):
            criar_geometria_brasil("fgv_emap.csv", "hello world")

    def test_função_geom_br3(self):
        #Se espera falha (ValueError está tratado)  

        with self.assertRaises(Exception):
            criar_geometria_brasil(10, 2)


if __name__ == "__main__":
    unittest.main()

#O teste condiz com o esperado, sendo 5 falhas em 7 testes.