import pandas as pd
import numpy as np
from utils_kauan import ler_csv, removing_columns_from_to, removing_list_columns, type_of_university
# Lendo csv
df_ens_sup = ler_csv("ed-superior-inep.csv")

# Dropando as colunas com drop
removing_list_columns(df_ens_sup, ["NU_ANO_CENSO", "CO_MUNICIPIO_IES", "CO_UF_IES", "CO_REGIAO_IES","NO_REGIAO_IES","NO_UF_IES", "NO_MUNICIPIO_IES", "IN_CAPITAL_IES", "TP_ORGANIZACAO_ACADEMICA"])

removing_columns_from_to(df_ens_sup, "NO_MANTENEDORA", "QT_LIVRO_ELETRONICO")
removing_columns_from_to(df_ens_sup, "QT_DOC_EX_INT", "NO_LOCAL_OFERTA")
removing_columns_from_to(df_ens_sup, "NO_MESORREGIAO_IES", "CO_MICRORREGIAO_IES")

type_of_university(df_ens_sup)

removing_list_columns(df_ens_sup, ["TP_CATEGORIA_ADMINISTRATIVA"])
