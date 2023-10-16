import pandas as pd

from read import base_inep
from selecting_data import select_data

print(select_data(base_inep, "amarela"))
mini_df = pd.DataFrame({
	"SG_UF_IES":["AC", "AL"],
	"QT_DOC_EX_AMARELA": [8, 66],
	"QT_DOC_EXE": [1286, 4912],
	"NO_REGIAO_IES": ["Norte", "Nordeste"],
	"AMARELA_RELACAO": [0.622, 1.343],
})
print(mini_df)

