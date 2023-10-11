import geopandas as gpd
import matplotlib.pyplot as plt
from tratamento_base import tratar_base

def customização_plot() -> None:
    '''Função para adicionar as customizações a serem aplicadas no plot
    '''

    plt.title("Número de Docentes de Ensino Superior por Estado ", fontsize=11)

def plotar_gráfico() -> None:
    '''Função que plota o gráfico
    '''
    dataframe_plot = tratar_base()
    dataframe_plot.plot(column = "QT_DOC_EXE",
                    cmap = "viridis",
                    legend = True)
    
    customização_plot()

    return plt.show()

