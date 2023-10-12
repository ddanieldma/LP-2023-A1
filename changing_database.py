from  setting_database import df_ens_sup



print(df_ens_sup)
df_por_regiao = df_ens_sup.drop(["NO_REGIAO_IES","Tipo_UNI_SPE", "NO_UF_IES", "NO_MUNICIPIO_IES", "IN_CAPITAL_IES", "TP_ORGANIZACAO_ACADEMICA", "TP_CATEGORIA_ADMINISTRATIVA"], axis=1)
df_por_regiao = df_por_regiao.groupby(by=["SG_UF_IES", "Tipo_UNI"]).sum()

total_doc_por_estado = df_por_regiao.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()
print(total_doc_por_estado)
df_por_regiao["PCT_DOUT_TOTAL"] = df_por_regiao["QT_DOC_EX_DOUT"]/total_doc_por_estado
df_por_regiao["PCT_MEST_TOTAL"] = df_por_regiao["QT_DOC_EX_MEST"]/total_doc_por_estado
df_por_regiao["PCT_ESP_TOTAL"] = df_por_regiao["QT_DOC_EX_ESP"]/total_doc_por_estado

print(df_por_regiao)

# Calcule a soma da porcentagem de doutores por estado
soma_por_estado = df_por_regiao.groupby(level='SG_UF_IES')['PCT_DOUT_TOTAL'].sum()

# Ordene o DataFrame com base nas somas em ordem decrescente
df_por_regiao = df_por_regiao.loc[soma_por_estado.sort_values(ascending=False).index]

# Número absoluto de doutores entre faculdades públicas e faculdades privadas
# porcentagem de dourtores
# porcentagem de mestrandos
# porcentagem de especializandos
# Por região?