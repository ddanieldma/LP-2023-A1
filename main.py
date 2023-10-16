import matplotlib.pyplot as plt

# from dados_chart_brancos import professores_brancos_raca_estado
# from dados_chart_negros import professores_negros_raca_estado

from selecting_data import selecting_data

from circular_chart import make_plot

from read import base_inep

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection="polar"))

# plot docentes brancos
docentes_brancos_estado = selecting_data(base_inep, "branca")
print(docentes_brancos_estado)
make_plot(docentes_brancos_estado, "Porcentagem de docentes brancos", "branca", ax1)

# plot docentes negros
docentes_negros_estado = selecting_data(base_inep, "negra")
make_plot(docentes_negros_estado, "Porcentagem de docentes negros", "negra", ax2)

plt.show()