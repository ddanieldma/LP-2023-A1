import geopandas as gpd
from tratamento_base import dataframe_plot
import matplotlib.pyplot as plt

dataframe_plot.plot(column = "QT_DOC_EXE",
                    cmap = "viridis",
                    legend = True)

plt.title("Número de Docentes de Ensino Superior por Estado ", fontsize=11)

plt.show()