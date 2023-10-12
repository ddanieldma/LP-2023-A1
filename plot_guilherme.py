'''Módulo que pega a base tratada e plota a visualização desejada
'''

import sys
import geopandas as gpd
import matplotlib.pyplot as plt
from tratamento_base import tratar_base

def customização_plot() -> None:
    """Função para adicionar as customizações a serem aplicadas no plot
    """
    plt.title("Número de Docentes de Ensino Superior por Estado ", fontsize=11)


def plotar_gráfico() -> None:
    """Função que plota o gráfico
    """
    dataframe_plot = tratar_base()

    try:
        ax = dataframe_plot.plot(column = "QT_DOC_EXE",
                        cmap = "viridis",
                        legend = True)
    except (ValueError, KeyError):
        print("coluna e/ou cmap não existem (criação do plot)")
        sys.exit(1)
        
    #Adicionando número (escrito) de docentes nos estados (rótulo)
    for x, y, label in zip(dataframe_plot.geometry.centroid.x, 
                           dataframe_plot.geometry.centroid.y, 
                           dataframe_plot["QT_DOC_EXE"]):
        
        try:
            ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white')
        except (NameError, ValueError):
            print("variáveis e/ou valores atribuídos não existem (criação do rótulo)")
            sys.exit(1)

    customização_plot()

    return plt.show()

plotar_gráfico()