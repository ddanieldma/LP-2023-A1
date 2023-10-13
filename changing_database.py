from  setting_database import df_ens_sup
from utils_kauan import  cria_porcentagem, cria_base_ordem_crescente, removing_columns_from_to

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
