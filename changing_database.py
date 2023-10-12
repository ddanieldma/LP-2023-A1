from  setting_database import df_ens_sup
from utils_kauan import agrupando_por_soma, cria_porcentagem, cria_base_ordem_crescente

df_por_regiao = agrupando_por_soma(df_ens_sup, "SG_UF_IES", "Tipo de Universidade")

total_doc_por_UF = df_por_regiao.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()

cria_porcentagem(df_por_regiao, "PCT_DOUT_TOTAL", "QT_DOC_EX_DOUT", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_MEST_TOTAL", "QT_DOC_EX_MEST", total_doc_por_UF)
cria_porcentagem(df_por_regiao, "PCT_ESP_TOTAL", "QT_DOC_EX_ESP", total_doc_por_UF)

df_dout = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_DOUT_TOTAL")
df_mest = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_MEST_TOTAL")
df_esp = cria_base_ordem_crescente(df_por_regiao, "Tipo de Universidade", "PCT_ESP_TOTAL")