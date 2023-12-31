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


class Test_utils_analyzing(unittest.TestCase):
    def test_cria_porcentagem(self):
        ## Teste com algo que existe

        # Criando as variáveis que precisamos pro dataframe
        data = pd.DataFrame({'QT_DOC_TOTAL': {('AC', 'Privada'): 339, ('AC', 'Pública'): 1002, ('AL', 'Privada'): 2370, ('AL', 'Pública'): 2690, ('AM', 'Privada'): 2088}, 'QT_DOC_EX_DOUT': {('AC', 'Privada'): 70, ('AC', 'Pública'): 522, ('AL', 'Privada'): 553, ('AL', 'Pública'): 1622, ('AM', 'Privada'): 427}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
        total_doc_por_UF = total_doc_por_UF = data.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()

        # Criando o dataframe que esperamos
        expected_output = pd.DataFrame({'QT_DOC_TOTAL': {('AC', 'Privada'): 339, ('AC', 'Pública'): 1002, ('AL', 'Privada'): 2370, ('AL', 'Pública'): 2690, ('AM', 'Privada'): 2088}, 'QT_DOC_EX_DOUT': {('AC', 'Privada'): 70, ('AC', 'Pública'): 522, ('AL', 'Privada'): 553, ('AL', 'Pública'): 1622, ('AM', 'Privada'): 427}, 'PCT_DOUT_TOTAL': {('AC', 'Privada'): 5.219985085756898, ('AC', 'Pública'): 38.92617449664429, ('AL', 'Privada'): 10.928853754940711, ('AL', 'Pública'): 32.055335968379445, ('AM', 'Privada'): 20.450191570881227}})
        expected_output = expected_output.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
        
        # Checando a igualdade entre os dois dataframes
        pd.testing.assert_frame_equal(cria_porcentagem(data, "PCT_DOUT_TOTAL", "QT_DOC_EX_DOUT", total_doc_por_UF), expected_output)
        
        ## Teste com uma coluna que não existe

        data = pd.DataFrame({'QT_DOC_TOTAL': {('AC', 'Privada'): 339, ('AC', 'Pública'): 1002, ('AL', 'Privada'): 2370, ('AL', 'Pública'): 2690, ('AM', 'Privada'): 2088}, 'QT_DOC_EX_DOUT': {('AC', 'Privada'): 70, ('AC', 'Pública'): 522, ('AL', 'Privada'): 553, ('AL', 'Pública'): 1622, ('AM', 'Privada'): 427}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
        total_doc_por_UF = total_doc_por_UF = data.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()
        
        # Definindo o output esperado
        expected_output = "O nome da coluna não existe"
        self.assertEqual(cria_porcentagem(data, "PCT_DOC_TOT", "nome_aleatorio", total_doc_por_UF), expected_output)

        ## Teste com algo que não é uma string

        # Definindo o dataframe
        data = pd.DataFrame({'QT_DOC_TOTAL': {('AC', 'Privada'): 339, ('AC', 'Pública'): 1002, ('AL', 'Privada'): 2370, ('AL', 'Pública'): 2690, ('AM', 'Privada'): 2088}, 'QT_DOC_EX_DOUT': {('AC', 'Privada'): 70, ('AC', 'Pública'): 522, ('AL', 'Privada'): 553, ('AL', 'Pública'): 1622, ('AM', 'Privada'): 427}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
        total_doc_por_UF = total_doc_por_UF = data.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()

        # Definindo o output esperado
        expected_output = "O nome da coluna não é uma string"

        # Checando a igualdade entre os dois
        self.assertEqual(cria_porcentagem(data, "PCT_DOC_TOT", 3, total_doc_por_UF), expected_output)

    def test_cria_base_ordem_crescente(self):
        ## Checando num dataframe normal 

        # Definindo o dataframe
        data = pd.DataFrame({'PCT_DOUT_TOTAL': {('AC', 'Privada'): 5.219985085756898, ('AC', 'Pública'): 38.92617449664429, ('AL', 'Privada'): 10.928853754940711, ('AL', 'Pública'): 32.055335968379445, ('AM', 'Privada'): 7.8463800073502386}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])

        # Definindo o output file
        expected_output = pd.DataFrame({'Privada': {'AM': 7.8463800073502386, 'AL': 10.928853754940711, 'AC': 5.219985085756898}, 'Pública': {'AM': np.nan, 'AL': 32.055335968379445, 'AC': 38.92617449664429}})
        expected_output = expected_output.rename_axis(["SG_UF_IES"])
        expected_output = expected_output.rename_axis("Tipo de Universidade", axis= "columns")

        # Checando a igualdade
        pd.testing.assert_frame_equal(cria_base_ordem_crescente(data, "Tipo de Universidade", "PCT_DOUT_TOTAL"), expected_output)

        # Chechando o tratamento de erro para colunas que não existem
        data = pd.DataFrame({'PCT_DOUT_TOTAL': {('AC', 'Privada'): 5.219985085756898, ('AC', 'Pública'): 38.92617449664429, ('AL', 'Privada'): 10.928853754940711, ('AL', 'Pública'): 32.055335968379445, ('AM', 'Privada'): 7.8463800073502386}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])

        # Definindo o output file
        expected_output = "O nome do index ou da coluna não existe no dataframe"

        # Fazendo o teste
        self.assertEqual(cria_base_ordem_crescente(data, "Tipo de Universidade", "qualquer_nome"), expected_output)

        # Erro caso não seja uma string
        data = pd.DataFrame({'PCT_DOUT_TOTAL': {('AC', 'Privada'): 5.219985085756898, ('AC', 'Pública'): 38.92617449664429, ('AL', 'Privada'): 10.928853754940711, ('AL', 'Pública'): 32.055335968379445, ('AM', 'Privada'): 7.8463800073502386}})
        data = data.rename_axis(["SG_UF_IES", "Tipo de Universidade"])

        # Definindo o output file
        expected_output = "O(s) nome(s) da(s) coluna(s) que você passou não é uma string"

        # Fazendo o teste
        self.assertEqual(cria_base_ordem_crescente(data, 1, 4), expected_output)

class Test_graphs(unittest.TestCase):
    def teste_formata_cada_plot(self):
        
        # como o retorno é um gráfico, não tem como comparar com o esperado

        # Checando o tratamento de exceções para se o título não é uma string
        axes = plt.subplots(1, 3, figsize=(15, 5))
        data = pd.DataFrame({"RJ":[1,2,3]})

        expected_output = "O título não é uma string"

        self.assertEqual(formata_cada_plot(data, 1, 1, axes), expected_output)

        ## Tratamento para se o número não é um inteiro
        axes = plt.subplots(1, 3, figsize=(15, 5))
        data = pd.DataFrame({"RJ":[1,2,3]})

        expected_output = "O número do plot não existe"

        self.assertEqual(formata_cada_plot(data, "Hello", 15, axes), expected_output)






if __name__== "__main__":
    unittest.main()