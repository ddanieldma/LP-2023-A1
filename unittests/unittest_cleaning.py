import sys
import os
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from functions.database.analyzing_functions import *
from functions.database.cleaning_functions import *
from functions.plotting.plotting import *
import unittest
import pandas as pd
import matplotlib.pyplot as plt

class Test_utils_cleaning(unittest.TestCase):
    
    def test_removing_list_columns(self):
        # Teste retirando uma lista de colunas
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = pd.DataFrame({"RJ": [1, 2, 3]})
        pd.testing.assert_frame_equal(removing_list_columns(data, ["SP", "RS", "SC"]), expected_output)
        
        # Teste retirando uma lista de colunas que não existe
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = "O nome da coluna não está no dataframe"
        self.assertEqual(removing_list_columns(data, ["DF", "RS", "SC"]), expected_output)

        # Teste retirando uma lista de colunas que não é uma lista
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = "Você não colocou uma lista de strings"
        self.assertEqual(removing_list_columns(data, "DF"), expected_output)

    def test_removing_columns_from_to(self):
        # Teste retirando as colunas de 1 a 3
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = pd.DataFrame({"SC":[10, 11, 12]})
        pd.testing.assert_frame_equal(removing_columns_from_to(data, "RJ", "RS"), expected_output)
        
        # Test case retirando as colunas de 4 a 2
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = pd.DataFrame({"RJ": [1, 2, 3]})
        pd.testing.assert_frame_equal(removing_columns_from_to(data, "SC", "SP"), expected_output)

        # Test case com nome de coluna que não existe
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = "A coluna informada não existe no dataframe"
        self.assertEqual(removing_columns_from_to(data, "DF", "SC"), expected_output) 

        # Teste case com a coluna não sendo string
        data = pd.DataFrame({"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]})
        expected_output = "O nome da coluna informada não é uma string"
        self.assertEqual(removing_columns_from_to(data, 1, "SC"), expected_output)

    def test_type_of_university(self):
        # Teste com um dataframe
        data = pd.DataFrame({"Universidade": ["UFRJ", "FGV", "PUC"], "TP_CATEGORIA_ADMINISTRATIVA": [1, 5, 6]})
        expected_output = pd.DataFrame({'Universidade': {0: 'UFRJ', 1: 'FGV', 2: 'PUC'}, 'TP_CATEGORIA_ADMINISTRATIVA': {0: 1, 1: 5, 2: 6}, 'Tipo de Universidade': {0: 'Pública', 1: 'Privada', 2: 'Privada'}})
        pd.testing.assert_frame_equal(type_of_university(data), expected_output)

        # Teste com uma coluna que não existe
        data = pd.DataFrame({"Universidade": ["UFRJ", "FGV", "PUC"], "TP_CATEGORIA_ADMINISTRATIVA": [1, 5, 6]})
        expected_output = "O nome da coluna não existe ou não é uma string"
        self.assertEqual(type_of_university(data, "TP"), expected_output)
