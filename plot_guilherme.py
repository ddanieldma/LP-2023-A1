import geopandas as gpd
from tratamento_base import dataframe_plot
import matplotlib.pyplot as plt

dataframe_plot.plot(column = "QT_DOC_EXE",
                    cmap = "Reds",
                    legend = True)
plt.show()