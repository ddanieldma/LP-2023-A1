import numpy as np

from read import base_inep

# agrupando por estado as quantidades de docentes de cada etnia e colocando a região de cada estado
estado_regioes = base_inep.groupby(["SG_UF_IES"])["NO_REGIAO_IES"].unique().reset_index()
professores_brancos_raca_estado = base_inep.groupby(["SG_UF_IES"])[["QT_DOC_EX_BRANCA", "QT_DOC_EXE"]].sum().reset_index()
professores_brancos_raca_estado = professores_brancos_raca_estado.merge(estado_regioes, how="left", on="SG_UF_IES")

# como os nomes das regiões ficam armazenados em ndarrays após o merge
# a seguinte linha de codigo extrai esses valores e coloca na coluna no
# lugar dos ndarrays
professores_brancos_raca_estado['NO_REGIAO_IES'] = professores_brancos_raca_estado['NO_REGIAO_IES'].apply(lambda x: x[0] if isinstance(x, np.ndarray) and len(x) == 1 else x)

print(professores_brancos_raca_estado)
# colocando colunas com a quantidade de professores de cada etnia em relação ao valor total de docentes
professores_brancos_raca_estado["brancos_relacao"] = (professores_brancos_raca_estado["QT_DOC_EX_BRANCA"] / professores_brancos_raca_estado["QT_DOC_EXE"]) * 100

professores_brancos_raca_estado_sorted = (
	professores_brancos_raca_estado
	.groupby(["NO_REGIAO_IES"])
	.apply(lambda x: x.sort_values(["brancos_relacao"], ascending=False))
	.reset_index(drop=True)
)

# Gráfico de barras circular
GROUP_brancos = professores_brancos_raca_estado_sorted["NO_REGIAO_IES"].values

VALUES_brancos = professores_brancos_raca_estado_sorted["brancos_relacao"].values
LABELS_brancos = professores_brancos_raca_estado_sorted["SG_UF_IES"].values
# 3 barras vazias
PAD_brancos = 2
# posições onde as barras estão localizadas
ANGLES_N_brancos = len(VALUES_brancos) + PAD_brancos * len(np.unique(GROUP_brancos))
ANGLES_brancos = np.linspace(0, 2 * np.pi, num=ANGLES_N_brancos, endpoint=False)
WIDTH_brancos = (2 * np.pi) / len(ANGLES_brancos)

GROUPS_SIZE_brancos = [len(regiao[1]) for regiao in professores_brancos_raca_estado.groupby("NO_REGIAO_IES")]

offset = 0
OFFSET_brancos = np.pi / 2
IDXS = []
for tamanho in GROUPS_SIZE_brancos:
	IDXS += list(range(offset + PAD_brancos, offset + tamanho + PAD_brancos))
	offset += tamanho + PAD_brancos