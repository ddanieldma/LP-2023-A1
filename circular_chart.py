import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# from dados_chart_brancos import *
# from dados_chart_negros import *

from utils import add_labels

# definindo multiplos plots circulares
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection="polar"))

def make_plot(dataframe: pd.DataFrame, title: str, etnia: int, axes) -> None:
	""" Cria a estrutura do plot dentro de um axes, que é um subplot que vai ser utilizado no gridplot final.

	:param pd.DataFrame dataframe: dataframe com os dados
	:param str title: título do subplot
	:param str etnia: etnia para a qual o plot será feito
	:param matplotlib.projections.polar.PolarAxes axes 
	"""
	etnia = etnia.upper()

	dataframe_sorted = (
		dataframe
		.groupby(["NO_REGIAO_IES"])
		.apply(lambda x: x.sort_values([etnia + "_RELACAO"], ascending=False))
		.reset_index(drop=True)
	)

	PADDING = 2
	OFFSET = np.pi / 2

	GROUP = dataframe_sorted["NO_REGIAO_IES"].values

	VALUES = dataframe_sorted[etnia + "_RELACAO"].values
	LABELS = dataframe_sorted["SG_UF_IES"].values
	
	ANGLES_N = len(VALUES) + PADDING * len(np.unique(GROUP))
	ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
	WIDTH = (2 * np.pi) / len(ANGLES)

	GROUPS_SIZE = [len(regiao[1]) for regiao in dataframe.groupby("NO_REGIAO_IES")]

	IDXS = []
	offset = 0
	for tamanho in GROUPS_SIZE:
		IDXS += list(range(offset + PADDING, offset + tamanho + PADDING))
		offset += tamanho + PADDING

	axes.set_title(title, verticalalignment="bottom")

	axes.set_theta_offset(OFFSET)

	# define limites para altura da barra, de forma que aja um buraco no meio
	axes.set_ylim(-100, 100)

	axes.set_frame_on(False)
	axes.xaxis.grid(False)
	axes.yaxis.grid(False)
	axes.set_xticks([])
	axes.set_rlabel_position(-355)
	axes.set_yticks([20, 40, 60, 80, 100])
	axes.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], fontsize=9)

	COLORS = [f"C{i}" for i, tamanho in enumerate(GROUPS_SIZE) for _ in range(tamanho)]

	axes.bar(
		ANGLES[IDXS], VALUES, width=WIDTH, linewidth=2,
		color=COLORS, edgecolor="#ffffff"
	)

	add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, axes)

	offset = 0
	for grupo, tamanho in zip(["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"], GROUPS_SIZE):
		x1 = np.linspace(ANGLES[offset + PADDING], ANGLES[offset + tamanho + PADDING - 1])
		axes.plot(x1, [-5] * 50, color="#333333")

		axes.text(
			np.mean(x1), -20, grupo, color="#333333", fontsize=8,
			fontweight="bold", ha="center", va="top"
		)

		# adicionando marcações de 20%, 40%, 60%, 80% e 100%
		x2 = np.linspace(ANGLES[offset], ANGLES[offset + tamanho + PADDING - 1], num=50)
		axes.plot(x2, [20] * 50, color="#bebebe", lw=0.8)
		axes.plot(x2, [40] * 50, color="#bebebe", lw=0.8)
		axes.plot(x2, [60] * 50, color="#bebebe", lw=0.8)
		axes.plot(x2, [80] * 50, color="#bebebe", lw=0.8)
		axes.plot(x2, [100] * 50, color="#bebebe", lw=0.8)

		offset += tamanho + PADDING