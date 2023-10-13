import pandas as pd
import numpy as np
from utils_kauan import *
# Lendo csv
df_ens_sup = ler_csv("ed-superior-inep.csv")

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
print(df_select.head().to_dict())
df_dout = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_DOUT_TOTAL")
df_mest = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_MEST_TOTAL")
df_esp = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_ESP_TOTAL")
