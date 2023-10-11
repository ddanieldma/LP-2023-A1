import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from read import base_inep

# selecionando dados
docentes_negros = base_inep.groupby(["SG_UF_IES"])["QT_DOC_EX_PRETA"].sum().reset_index()
estados = list(base_inep["SG_UF_IES"].unique())
estados = sorted(estados)

# figure
fig, ax = plt.subplots(figsize =(16, 9))

# gráfico de barras
plt.bar(estados, docentes_negros["QT_DOC_EX_PRETA"])

# Personalização
# remove axis splines
for spline in ['top', 'left', 'right']:
	ax.spines[spline].set_visible(False)

# Remove x, y ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# Add x, y gridlines
ax.grid(color ='grey', linestyle ='-.',
		linewidth = 0.5, alpha = 0.2)

# Show top values
ax.invert_yaxis()

# Add annotations to bars
for barra in ax.patches:
	plt.text(barra.get_width()+0.2, barra.get_y()+0.5,
		  str(round((barra.get_width()), 2)),
		  fontsize=10, fontweight='bold',
		  color='grey')

# Add plot title
ax.set_title("Quantidade de professores negros no ensino superior por estado",
			 loc="left")

# Text watermark
fig.text(0.9, 0.15, "Jeeteshgavande30", fontsize=12,
		 color="grey", ha='right', va='bottom',
		 alpha=0.7)

plt.show()