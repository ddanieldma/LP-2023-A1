'''Módulo que pega a base tratada e plota a visualização desejada
'''


import sys
sys.path.append("../database")
import geopandas as gpd
import matplotlib.pyplot as plt
from functions.database.tratamento_base import *

def customização_plot() -> None:
    """Função para adicionar as customizações a serem aplicadas no plot
    """
    plt.title("Número de Docentes de Ensino Superior por Estado", fontsize=12, color="darkblue", family="arial")

    # Remover ticks dos eixos
    plt.xticks([])
    plt.yticks([])

    # Adicionar cor de fundo
    plt.gca().set_facecolor('lightblue')

def plotar_gráfico(dataframe) -> None:
    """Função que plota o gráfico
    """
    try:
        ax = dataframe.plot(column="QT_DOC_EXE", cmap="viridis", legend=True)
    except (ValueError, KeyError):
        print("coluna e/ou cmap não existem (criação do plot)")
        sys.exit(1)
        
    # Adicionando número (escrito) de docentes nos estados (rótulo)
    for x, y, label in zip(dataframe.geometry.centroid.x, dataframe.geometry.centroid.y, dataframe["QT_DOC_EXE"]):
        # Pequeno tratamento das cores (branco fica pouco legível no amarelo)
        if label == 72466:
            color = "black"
        else:
            color = "white"
        
        try:
            ax.text(x, y, label, fontsize=6, ha='center', va='center', color=color)
        except (NameError, ValueError):
            return "variáveis e/ou valores atribuídos não existem (criação do rótulo)"

    customização_plot()

    plt.show()  # Mostrar o gráfico uma única vez


