''' Módulo destinado a realizar os unittest das funções de leitura de arquivos
'''

import unittest
import geopandas as gpd
import pandas as pd
from functions.database.read import *

class TesteFunçõesMain(unittest.TestCase):

    def test_função_read1(self):
    
        true_df = ler_csv("csv1_unittest.csv")
        dados1 = {"estado":["MG", "SP", "RJ"], "DDD":[32, 11, 21]}
        df_teste_1 = pd.DataFrame(dados1)
        #dataframes iguais

        pd.testing.assert_frame_equal(true_df, df_teste_1)
        
        #passando caminho que não resulta em um csv
        output_esperado = "Arquivo não encontrado"
        self.assertEqual(ler_csv("fgv_emap.csv"), output_esperado)

        #passando caminho que não é uma string
        output_esperado = "O caminho deve ser uma string"
        self.assertEqual(ler_csv(8), output_esperado)

    def test_função_geom_br1(self):

        geodf = criar_geometria_brasil("bcim_2016_21_11_2018.gpkg", "lim_unidade_federacao_a")

        #Não se espera falha (resultado deve ser um GeoDataFrame)
        self.assertIsInstance(geodf, gpd.GeoDataFrame)

        #passando arquivo e coluna de arquivo que não existem
        output_esperado = "O arquivo e/ou a coluna layer não existe/existem"
        self.assertEqual(criar_geometria_brasil("bcim_2016_21_11_2018.gpkg", "pikachu"), output_esperado)        

        self.assertEqual(criar_geometria_brasil("ventilador", "lim_unidade_federacao_a"), output_esperado)  

        #passando argumento que não é string
        output_esperado = "ambos os valores devem ser strings"
        self.assertEqual(criar_geometria_brasil("bcim_2016_21_11_2018.gpkg", 2.0), output_esperado)        


if __name__ == "__main__":
    unittest.main()

