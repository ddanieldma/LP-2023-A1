import numpy as np

from read import base_inep

from auxiliary import *

# agrupando por estado as quantidades de docentes de cada etnia e colocando a região de cada estado
estado_regioes = base_inep.groupby(["SG_UF_IES"])["NO_REGIAO_IES"].unique().reset_index()
professores_negros_raca_estado = base_inep.groupby(["SG_UF_IES"])[["QT_DOC_EX_PRETA", "QT_DOC_EX_PARDA", "QT_DOC_EXE"]].sum().reset_index()
professores_negros_raca_estado = professores_negros_raca_estado.merge(estado_regioes, how="left", on="SG_UF_IES")

# como os nomes das regiões ficam armazenados em ndarrays após o merge
# a seguinte linha de codigo extrai esses valores e coloca na coluna no
# lugar dos ndarrays
professores_negros_raca_estado['NO_REGIAO_IES'] = professores_negros_raca_estado['NO_REGIAO_IES'].apply(lambda x: x[0] if isinstance(x, np.ndarray) and len(x) == 1 else x)

print(professores_negros_raca_estado)
# colocando colunas com a quantidade de professores de cada etnia em relação ao valor total de docentes
professores_negros_raca_estado["negros_relacao"] = ((professores_negros_raca_estado["QT_DOC_EX_PRETA"] + professores_negros_raca_estado["QT_DOC_EX_PARDA"]) / professores_negros_raca_estado["QT_DOC_EXE"]) * 100

professores_negros_raca_estado_sorted = (
	professores_negros_raca_estado
	.groupby(["NO_REGIAO_IES"])
	.apply(lambda x: x.sort_values(["negros_relacao"], ascending=False))
	.reset_index(drop=True)
)

# Gráfico de barras circular
GROUP_negros = professores_negros_raca_estado_sorted["NO_REGIAO_IES"].values

VALUES_negros = professores_negros_raca_estado_sorted["negros_relacao"].values
LABELS_negros = professores_negros_raca_estado_sorted["SG_UF_IES"].values
# 3 barras vazias
PAD_negros = 2
# posições onde as barras estão localizadas
ANGLES_N_negros = len(VALUES_negros) + PAD_negros * len(np.unique(GROUP_negros))
ANGLES_negros = np.linspace(0, 2 * np.pi, num=ANGLES_N_negros, endpoint=False)
WIDTH_negros = (2 * np.pi) / len(ANGLES_negros)

GROUPS_SIZE_negros = [len(regiao[1]) for regiao in professores_negros_raca_estado.groupby("NO_REGIAO_IES")]

offset = 0
OFFSET_negros = np.pi / 2
IDXS = []
for tamanho in GROUPS_SIZE_negros:
	IDXS += list(range(offset + PAD_negros, offset + tamanho + PAD_negros))
	offset += tamanho + PAD_negros