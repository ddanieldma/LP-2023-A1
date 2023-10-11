import geopandas as gpd
from tratamento_base import tratar_base
import matplotlib.pyplot as plt

def customização_plot():
    plt.title("Número de Docentes de Ensino Superior por Estado ", fontsize=11)
    return True

def plotar_gráfico():
    dataframe_plot = tratar_base()
    dataframe_plot.plot(column = "QT_DOC_EXE",
                    cmap = "viridis",
                    legend = True)
    
    customização_plot()

    return plt.show()

plotar_gráfico()
