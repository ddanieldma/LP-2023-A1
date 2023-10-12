import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dados_chart_brancos import *
from dados_chart_negros import *

from auxiliary import add_labels

# definindo multiplos plots circulares
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection="polar"))

#==================================================================
# Primeiro plot, para docentes brancos
ax1.set_title("Porcentagem de docentes brancos", verticalalignment="bottom")

ax1.set_theta_offset(OFFSET_brancos)

# define limites para altura da barra, de forma que aja um buraco no meio
ax1.set_ylim(-100, 100)

ax1.set_frame_on(False)
ax1.xaxis.grid(False)
ax1.yaxis.grid(False)
ax1.set_xticks([])
ax1.set_rlabel_position(-355)
ax1.set_yticks([20, 40, 60, 80, 100])
ax1.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], fontsize=9)

GROUPS_SIZE = [len(regiao[1]) for regiao in professores_brancos_raca_estado.groupby("NO_REGIAO_IES")]
COLORS = [f"C{i}" for i, tamanho in enumerate(GROUPS_SIZE) for _ in range(tamanho)]

ax1.bar(
	ANGLES_brancos[IDXS], VALUES_brancos, width=WIDTH_brancos, linewidth=2,
	color=COLORS, edgecolor="#ffffff"
)

add_labels(ANGLES_brancos[IDXS], VALUES_brancos, LABELS_brancos, OFFSET_brancos, ax1)

offset = 0
for grupo, tamanho in zip(["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"], GROUPS_SIZE):
	x1 = np.linspace(ANGLES_brancos[offset + PAD_brancos], ANGLES_brancos[offset + tamanho + PAD_brancos - 1])
	ax1.plot(x1, [-5] * 50, color="#333333")

	ax1.text(
		np.mean(x1), -20, grupo, color="#333333", fontsize=8,
		fontweight="bold", ha="center", va="top"
	)

	# adicionando marcações de 20%, 40%, 60%, 80% e 100%
	x2 = np.linspace(ANGLES_brancos[offset], ANGLES_brancos[offset + tamanho + PAD_brancos - 1], num=50)
	ax1.plot(x2, [20] * 50, color="#bebebe", lw=0.8)
	ax1.plot(x2, [40] * 50, color="#bebebe", lw=0.8)
	ax1.plot(x2, [60] * 50, color="#bebebe", lw=0.8)
	ax1.plot(x2, [80] * 50, color="#bebebe", lw=0.8)
	ax1.plot(x2, [100] * 50, color="#bebebe", lw=0.8)

	offset += tamanho + PAD_brancos

#==================================================================
# Segundo plot, para docentes brancos
ax2.set_title("Porcentagem de docentes negros")

ax2.set_theta_offset(OFFSET_negros)

# define limites para altura da barra, de forma que aja um buraco no meio
ax2.set_ylim(-100, 100)

ax2.set_frame_on(False)
ax2.xaxis.grid(False)
ax2.yaxis.grid(False)
ax2.set_xticks([])
ax2.set_rlabel_position(-355)
ax2.set_yticks([20, 40, 60, 80, 100])
ax2.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], fontsize=9)

GROUPS_SIZE = [len(regiao[1]) for regiao in professores_negros_raca_estado.groupby("NO_REGIAO_IES")]
COLORS = [f"C{i}" for i, tamanho in enumerate(GROUPS_SIZE) for _ in range(tamanho)]

ax2.bar(
	ANGLES_negros[IDXS], VALUES_negros, width=WIDTH_negros, linewidth=2,
	color=COLORS, edgecolor="#ffffff"
)

add_labels(ANGLES_negros[IDXS], VALUES_negros, LABELS_negros, OFFSET_negros, ax2)

offset = 0
for grupo, tamanho in zip(["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"], GROUPS_SIZE):
	x1 = np.linspace(ANGLES_negros[offset + PAD_negros], ANGLES_negros[offset + tamanho + PAD_negros - 1])
	ax2.plot(x1, [-5] * 50, color="#333333")

	ax2.text(
		np.mean(x1), -20, grupo, color="#333333", fontsize=8,
		fontweight="bold", ha="center", va="top"
	)

	# adicionando marcações de 20%, 40%, 60%, 80% e 100%
	x2 = np.linspace(ANGLES_negros[offset], ANGLES_negros[offset + tamanho + PAD_negros - 1], num=50)
	ax2.plot(x2, [20] * 50, color="#bebebe", lw=0.8)
	ax2.plot(x2, [40] * 50, color="#bebebe", lw=0.8)
	ax2.plot(x2, [60] * 50, color="#bebebe", lw=0.8)
	ax2.plot(x2, [80] * 50, color="#bebebe", lw=0.8)
	ax2.plot(x2, [100] * 50, color="#bebebe", lw=0.8)

	offset += tamanho + PAD_negros

plt.show()