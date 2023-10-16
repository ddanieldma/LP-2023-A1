import sys
sys.path.append("..\LP-2023-A1")

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# plot kauan
from functions.database.analyzing_functions import *
from functions.database.cleaning_functions import *
from functions.plotting.plotting import *

# plot guilherme
from functions.database.tratamento_base import *
from functions.plotting.plot_guilherme import *

# plot daniel
from functions.database.selecting_data import select_data
from functions.plotting.circular_chart import make_plot

from functions.database.read import *

# Lendo csv
df_ens_sup = ler_csv("bases_de_dados/ed-superior-inep.csv")

geometria_brasil = criar_geometria_brasil("bases_de_dados/bcim_2016_21_11_2018.gpkg", "lim_unidade_federacao_a")

# Dropando as colunas com drop
removing_list_columns(df_ens_sup, ["NU_ANO_CENSO", "CO_MUNICIPIO_IES", "CO_UF_IES", "CO_REGIAO_IES","NO_REGIAO_IES","NO_UF_IES", "NO_MUNICIPIO_IES", "IN_CAPITAL_IES", "TP_ORGANIZACAO_ACADEMICA"])

removing_columns_from_to(df_ens_sup, "NO_MANTENEDORA", "QT_LIVRO_ELETRONICO")
removing_columns_from_to(df_ens_sup, "QT_DOC_EX_INT", "NO_LOCAL_OFERTA")
removing_columns_from_to(df_ens_sup, "NO_MESORREGIAO_IES", "CO_MICRORREGIAO_IES")

type_of_university(df_ens_sup)

removing_list_columns(df_ens_sup, ["TP_CATEGORIA_ADMINISTRATIVA"])

### Setting

# Agrupando por unidade federativa e por tipo de universidade
df_por_regiao = df_ens_sup.groupby(by=["SG_UF_IES", "Tipo de Universidade"]).sum()

# Somando a quantidade de docentes por UF
total_doc_por_UF = df_por_regiao.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()

cria_porcentagem(df_por_regiao, "PCT_DOUT_TOTAL", "QT_DOC_EX_DOUT", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_MEST_TOTAL", "QT_DOC_EX_MEST", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_ESP_TOTAL", "QT_DOC_EX_ESP", total_doc_por_UF)

df_select = df_por_regiao[["PCT_DOUT_TOTAL"]]

df_dout = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_DOUT_TOTAL")
df_mest = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_MEST_TOTAL")
df_esp = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_ESP_TOTAL")

# Crie um grid de subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

formata_cada_plot(df_esp, "Professores especializados por UF", 0, axes)
formata_cada_plot(df_mest, "Professores com mestrado por UF", 1, axes)
formata_cada_plot(df_dout, "Professores com doutorado por UF", 2, axes)

# Exiba o grid plot
plt.tight_layout()
plt.savefig("graficos/percentuais_de_docentes.png")

datagui = tratar_base(df_ens_sup, geometria_brasil)
plotar_gráfico(datagui)

#================================================================================
# plot daniel
fig, ax = plt.subplots(1, 2, subplot_kw=dict(projection="polar"), figsize=(10, 5))

# plot docentes brancos
docentes_brancos_estado = select_data(df_ens_sup, "branca")
make_plot(docentes_brancos_estado, "Porcentagem de docentes brancos por estado", "branca", ax[0])

# plot docentes negros
docentes_negros_estado = select_data(df_ens_sup, "negra")
make_plot(docentes_negros_estado, "Porcentagem de docentes negros por estado", "negra", ax[1])

# docentes_amarelos_estado = select_data(df_ens_sup, "amarela")
# make_plot(docentes_amarelos_estado, "Porcentagem de docentes amarelos por estado", "amarela", ax[1, 0])

# docentes_indigenas_estado = select_data(df_ens_sup, "indigena")
# make_plot(docentes_indigenas_estado, "Porcentagem de docentes indigenas por estado", "indigena", ax[1, 1])

fig.tight_layout(pad=10.0)
plt.savefig("graficos/percentuais_docentes_raca.png")