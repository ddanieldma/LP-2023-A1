from  setting_database import df_ens_sup
from utils_kauan import agrupando_por_soma, cria_porcentagem

df_por_regiao = agrupando_por_soma(df_ens_sup, "SG_UF_IES", "TIPO_UNI")

total_doc_por_UF = df_por_regiao.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()
print(total_doc_por_UF)

cria_porcentagem(df_por_regiao, "PCT_DOUT_TOTAL", "QT_DOC_EX_DOUT", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_MEST_TOTAL", "QT_DOC_EX_MEST", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_ESP_TOTAL", "QT_DOC_EX_ESP", total_doc_por_UF)

print(df_por_regiao)

#Reorganize os dados para criar um DataFrame de barras aninhadas
df_por_regiao = df_por_regiao.unstack('TIPO_UNI')['PCT_DOUT_TOTAL']

# Calcule a soma da porcentagem de doutorados por estado
soma_por_estado = df_por_regiao.sum(axis=1)

# Ordene os estados com base na soma das porcentagens em ordem decrescente
df_por_regiao = df_por_regiao.loc[soma_por_estado.sort_values(ascending=True).index]
