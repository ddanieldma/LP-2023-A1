import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from read import base_inep

por_regiao = base_inep.groupby(["NO_REGIAO_IES"]).sum().reset_index()
professores_raca_e_regiao = por_regiao[["QT_DOC_EX_BRANCA", "QT_DOC_EX_PRETA",
										"QT_DOC_EX_PARDA", "QT_DOC_EX_AMARELA",
										"QT_DOC_EX_INDIGENA", "NO_REGIAO_IES"]]
professores_brancos_estado = base_inep.groupby(["SG_UF_IES"])["QT_DOC_EX_BRANCA"].sum().reset_index()

def add_populacao_regioes(dicionario_populacoes: dict, df: pd.DataFrame) -> pd.DataFrame:


print(professores_raca_e_regiao)

# # Função auxiliar para rotação e alinhamento dos labels.
# def get_label_rotation(angle, offset):
# 	rotation = np.rad2deg(angle + offset)
# 	if angle <= np.pi:
# 		alignment = "right"
# 		rotation = rotation + 180
# 	else: 
# 		alignment = "left"
# 	return rotation, alignment

# # Função que adiciona os labels
# def add_labels(angles, values, labels, offset, ax):

# 	#espaço entre fim da barra e o label
# 	padding = 4

# 	for angle, value, label in zip(angles, values, labels):
# 		angle = angle

# 		# obtendo rotação e alinhamento
# 		rotation, alingment = get_label_rotation(angle, offset)

# 		ax.text(
# 			x=angle,
# 			y=value + padding,
# 			s=label,
# 			ha=alingment,
# 			va="center",
# 			rotation=rotation,
# 			rotation_mode="anchor"
# 		)

# # Gráfico de barras circular
# # posições onde as barras estão localizadas
# ANGLES = np.linspace(0, 2 * np.pi,
# 					 len(professores_brancos_estado), endpoint=False)
# VALUES = professores_brancos_estado["QT_DOC_EX_BRANCA"].values
# LABELS = professores_brancos_estado["SG_UF_IES"].values
# # VALUES = list(professores_brancos_estado["QT_DOC_EX_BRANCA"].values)
# # LABELS = list(professores_brancos_estado["SG_UF_IES"].values)

# # determina largura de cada barra dividindo dois pi pelo numero de barras
# WIDTH = 2 * np.pi / len(VALUES)

# # Determina onde colocar a primeira barra, começando em 90º. Por padrão o
# # matplotlib inicia em 0
# OFFSET = np.pi / 2

# fig, ax = plt.subplots(figsize=(200, 100), subplot_kw={"projection": "polar"})

# # offset especial
# ax.set_theta_offset(OFFSET)

# # define limites para altura da barra, de forma que aja um buraco no meio
# ax.set_ylim(-100, 100000)

# ax.set_frame_on(False)

# ax.xaxis.grid(False)
# ax.yaxis.grid(False)
# ax.set_xticks([])
# ax.set_yticks([])

# ax.bar(
# 	ANGLES, VALUES, width=WIDTH, linewidth=2,
# 	color="#6ce5e8", edgecolor="white"
# )

# add_labels(ANGLES, VALUES, LABELS, OFFSET, ax)

# plt.show()