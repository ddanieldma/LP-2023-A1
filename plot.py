import matplotlib.pyplot as plt
from changing_database import df_por_regiao

# Crie um gráfico de barras aninhado
ax = df_por_regiao.plot(kind='bar', stacked=True)

# Personalize os rótulos e o título do gráfico
plt.xlabel('Estado')
plt.ylabel('Porcentagem de Doutorados')
plt.title('Porcentagem de Doutorados por Tipo de Instituição por Estado')

# Exiba o gráfico
plt.show()