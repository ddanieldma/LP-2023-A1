import numpy as np
import pandas as pd

from read import base_inep

from utils import *

def selecting_data(dataframe: pd.DataFrame, etnia: str) -> pd.DataFrame:
	"""Seleciona os dados para a raça escolhida

	:param pd.DataFrame dataframe
	"""
	
	try:
		if not check_ethnicity(etnia):
			raise ValueError
	except ValueError:
		print("Etnia inválida")
		return None

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