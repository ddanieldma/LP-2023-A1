import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from read import base_inep

# removendo as 13 primeiras colunas
# base_reduzida = base_inep.drop(base_inep.iloc[:, 0:14], axis=1)
# base_reduzida.drop(base_reduzida.loc[:, "IN_ACESSO_PORTAL_CAPES":"QT_LIVRO_ELETRONICO"].columns, inplace=True, axis=1)
# print(base_reduzida)

# selecionando dados
docentes_negros = base_inep.groupby(["SG_UF_IES"])["QT_DOC_EX_PRETA"].sum().reset_index()
estados = list(base_inep["SG_UF_IES"].unique())
estados = sorted(estados)

# figure
fig = plt.figure(figsize =(10, 7))

# gráfico de barras
plt.bar(estados, docentes_negros["QT_DOC_EX_PRETA"])

plt.show()