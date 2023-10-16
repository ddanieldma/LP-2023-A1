'''Módulo que seleciona os dados na base
'''

import numpy as np
import pandas as pd

import os
import sys
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from database.utils import *

def select_data(dataframe: pd.DataFrame, etnia: str) -> pd.DataFrame:
	"""Seleciona na base os dados relatvios à etnia escolhida

	:param pd.DataFrame dataframe: base de dados
	:param str etnia: a etnia para a qual os dados serão selecionados na base

	:returns: um dataframe somente com as colunas necessárias para o plot
	
	:rtype: pd.DataFrame

	Exemplo:
	>>> df = pd.DataFrame({"RJ": [1, 2, 3]})
	>>> select_data(df, "caju")
	'etnia invalida'

	>>> select_data(df, 5)
	'a etnia precisa de ser uma string'
	"""
	
	try:
		if not check_ethnicity(etnia):
			raise ValueError
		if not isinstance(etnia, str):
			raise TypeError
	except ValueError:
		return "etnia invalida" 
	except TypeError:
		return "a etnia precisa de ser uma string"

	etnia = etnia.upper()

	# agrupando por estado as quantidades de docentes de cada etnia e colocando a região de cada estado
	estado_regioes = dataframe.groupby(["SG_UF_IES"])["NO_REGIAO_IES"].unique().reset_index()

	if etnia in ["PRETA", "PARDA", "NEGRA"]:
		docentes_raca_estado = dataframe.groupby(["SG_UF_IES"])[["QT_DOC_EX_PRETA", "QT_DOC_EX_PARDA", "QT_DOC_EXE"]].sum().reset_index()
	else:
		docentes_raca_estado = dataframe.groupby(["SG_UF_IES"])[["QT_DOC_EX_" + etnia, "QT_DOC_EXE"]].sum().reset_index()

	docentes_raca_estado = docentes_raca_estado.merge(estado_regioes, how="left", on="SG_UF_IES")

	# como os nomes das regiões ficam armazenados em ndarrays após o merge
	# a seguinte linha de codigo extrai esses valores e coloca na coluna no
	# lugar dos ndarrays
	docentes_raca_estado['NO_REGIAO_IES'] = docentes_raca_estado['NO_REGIAO_IES'].apply(lambda x: x[0] if isinstance(x, np.ndarray) and len(x) == 1 else x)
	
	# colocando colunas com a quantidade de professores de cada etnia em relação ao valor total de docentes
	if etnia in ["PRETA", "PARDA", "NEGRA"]:
		docentes_raca_estado[etnia + "_RELACAO"] = ((docentes_raca_estado["QT_DOC_EX_PRETA"] + docentes_raca_estado["QT_DOC_EX_PARDA"]) / docentes_raca_estado["QT_DOC_EXE"]) * 100
	else:
		docentes_raca_estado[etnia + "_RELACAO"] = (docentes_raca_estado["QT_DOC_EX_" + etnia]/ docentes_raca_estado["QT_DOC_EXE"]) * 100

	return docentes_raca_estado

if __name__ == "__main__":
	doctest.testmod(verbose=True)