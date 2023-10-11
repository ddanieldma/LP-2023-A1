import pandas as pd

def get_populacao_estados() -> pd.DataFrame:

	populacao_estados = pd.read_csv("populacoes_estados_2022.csv")

	# selecionando apenas colunas com estado e população
	populacao_estados = populacao_estados[["populacao_2022", "uf"]]

	# colocando siglas dos estados no dataframe
	dicionario_siglas_estados = {
		"São Paulo": "SP",
		"Minas Gerais": "MG",
		"Rio de Janeiro": "RJ",
		"Bahia": "BA",
		"Paraná": "PA",
		"Rio Grande do Sul": "RS",
		"Pernambuco": "PE",
		"Ceará": "CE",
		"Pará": "PA",
		"Santa Catarina": "SC",
		"Goiás": "GO",
		"Maranhão": "MA",
		"Paraíba": "PB",
		"Amazonas": "AM",
		"Espírito Santo": "ES",
		"Mato Grosso": "MT",
		"Rio Grande do Norte": "RN",
		"Piauí": "PI",
		"Alagoas": "AL",
		"Distrito Federal": "DF",
		"Mato Grosso do Sul": "MS",
		"Sergipe": "SE",
		"Rondônia": "RO",
		"Tocantins": "TO",
		"Acre": "AC",
		"Amapá": "AM",
		"Roraima": "RR",
	}
	siglas_estados = pd.DataFrame.from_dict(dicionario_siglas_estados, orient="index")
	populacao_estados["sg_uf"] = siglas_estados[0].values

	return populacao_estados

def get_populacao_regioes() -> pd.DataFrame:
	populacao_regioes = pd.read_csv("populacoes_regioes_2022.csv")

	# selecinando apenas colunas da regiao e da população
	populacao_regioes = populacao_regioes[["regiao", "populacao"]]

	dicionario_nomes_regioes = {
		"Região Norte": "Norte",
		"Região Nordeste": "Nordeste",
		"Região Sudeste": "Sudeste",
		"Região Sul": "Sul",
		"Região Centro-oeste": "Centro-Oeste",
	}
	nomes_regioes = pd.DataFrame.from_dict(dicionario_nomes_regioes, orient="index")
	populacao_regioes["regiao_resumido"] = nomes_regioes[0].values

	return populacao_regioes

populacao_regioes = get_populacao_regioes()
populacao_estados = get_populacao_estados()

if __name__ == "__main__":
	# print(populacao_estados)
	print(populacao_regioes)