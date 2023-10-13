import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from setting_database import df_dout, df_mest, df_esp
from utils_kauan import formata_cada_plot

# Crie um grid de subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

formata_cada_plot(df_esp, "Professores especializados por UF", 0, axes)
formata_cada_plot(df_mest, "Professores com mestrado por UF", 1, axes)
formata_cada_plot(df_dout, "Professores com doutorado por UF", 2, axes)

# Exiba o grid plot
plt.tight_layout()
plt.show()
