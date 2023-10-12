import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import doctest

def ler_csv(caminho_csv):
    return pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')

def removing_list_columns(dataframe: pd.DataFrame, lista: list) -> pd.DataFrame:
    """Essa função serve para remover uma lista de colunas de um dataframe

    :param pd.DataFrame dataframe: O dataframe do qual se deseja retirar as colunas
    :param lista list: Lista com os nomes das colunas a serem retiradas 

    :returns: Dataframe com as colunas especificadas removidas
    :rtype: pd.DataFrame

    Exemplo:
    >>> dados = {"RJ": [1, 2, 3], "SP": [4, 5, 6]}
    >>> df = pd.DataFrame(dados)
    >>> df = removing_list_columns(df, ["SP"])
    >>> df
       RJ
    0   1
    1   2
    2   3
    """

    try:
        # Tira as colunas do Dataframe
        dataframe.drop(lista, axis=1, inplace=True)
    except KeyError as error:
        return str("O nome da coluna não está no dataframe ou você não passou uma lista de strings")
    except Exception as error:
        return f"Houve um erro. Por favor, tente novamente:{error}"
    else:
        # Retorna o novo dataframe
        return dataframe



def removing_columns_from_to(dataframe: pd.DataFrame, start_col: str, end_col: str) -> pd.DataFrame:
    """ Essa função serve para remover todas as colunas entre um coluna e outra incluindo estas colunas
    :param pd.DataFrame dataframe: O dataframe do qual se deseja retirar as colunas
    :param str star_col: uma string com o nome da coluna a qual se deseja começar a retirar
    :param str end_col: uma string com o nome da coluna a qual se deseja terminar de retirar

    :returns: Dataframe removendo-se todas as colunas entre as colunas especificadas
    :rtype: pd.DataFrame 
    >>> dados = {"RJ": [1, 2, 3], "SP": [4, 5, 6], "RS":[7, 8, 9], "SC":[10, 11, 12]}
    >>> df = pd.DataFrame(dados)
    >>> df = removing_columns_from_to(df, "RJ", "RS")
    >>> df
       SC
    0  10
    1  11
    2  12
    """
    try:    
        # Pegando o índice das colunas que queremos retirar
        beginning_col = dataframe.columns.get_loc(start_col)
        finish_col = dataframe.columns.get_loc(end_col)

        # Selecionando o nome das colunas para retirar
        cols_to_drop = dataframe.columns[beginning_col:finish_col+1]

        #
        dataframe.drop(cols_to_drop, axis=1, inplace=True)
    except NameError:
        return "O dataframe não existe"
    except KeyError:
        return "A coluna informada não existe no dataframe"
    except TypeError:
        return "Os elementos não são uma string"
    else:
        return dataframe


# Dizendo se é pública ou privada
def type_of_university(dataframe: pd.DataFrame, column: str = "TP_CATEGORIA_ADMINISTRATIVA", nome_coluna_nova: str = "Tipo de Universidade") -> pd.DataFrame:
    """ Define o tipo de universidade entre pública e privada com base num dicionário feito pelo MEC, que vai de 1 à 9, sendo de 1 a 3 para escolas públicas e de 4 até 9 para escolas privadas

    :param pd.DataFrame dataframe: O dataframe do qual se deseja adicionar a coluna com o tipo de universidade
    :param str column: A coluna a qual se deseja retirar os dados para analisar (Opcional, padrão é "TP_CATEGORIA_ADMINISTRATIVA", o qual é a coluna para nossa base de dados)
    :param str nome_coluna_nova: O nome da nova coluna que se deseja criar (Opcional, padrão é "Tipo de Universidade", o qual é o nome que desejamos nomear nossa coluna)

    :return: Dataframe com uma coluna adicionada, informando se a escola é pública ou privada
    :rtype: pd.DataFrame

    """
    try: 
        # Dicionário com o tipo de escola
        types_of_universities = {1: "Pública", 2:"Pública", 3: "Pública", 4: "Privada", 5:"Privada", 6:"Privada", 7: "Privada", 8: "Privada", 9: "Privada"}
        
        # Adicionando a nova coluna
        dataframe[nome_coluna_nova] = dataframe[column].map(types_of_universities)
    except NameError:
        print("O dataframe especificado não existe")

    # Retorna o dataframe
    return dataframe

######################################################################################
# Análise
def agrupando_por_soma(dataframe: pd.DataFrame, arg1: str, arg2: str) -> pd.DataFrame:
    """ Funcão para agupar dois dados iguais e soma-los

    :param pd.DataFrame dataframe: O dataframe do qual se deseja agrupar por soma
    :param str arg1: Primeiro argumento o qual se deseja agrupar para somar
    :param str arg2: Segundo argumento o qual se deseja agrupar para somar

    :return: Retorna o Dataframe com as colunas somadas, com base nas colunas especificadas
    :rtype: pd.DataFrame
    
    """
    # Agrupando e somando com base no especificado
    dataframe = dataframe.groupby(by=[arg1, arg2]).sum()
    
    # Retornando o Dataframe
    return dataframe

def cria_porcentagem(dataframe: pd.DataFrame, nome_col: str, num_doc_esp: str, total_por_UF: pd.DataFrame):
    """ Cria uma coluna porcentagem com base em outras colunas do dataframe

    :param pd.DataFrame dataframe: O dataframe do qual se deseja adicionar a coluna com a porcentagem
    :param str nome_col: O nome da coluna que queremos adicionar
    :param str num_doc_esp: O nome da coluna a qual desejamos saber a porcentagem
    :param pd.DataFrame total_por_UF: Dataframe com o total de docentes por UF

    :return: O dataframe com uma coluna a mais com a a porcentagem devida
    :rtype: pd.DataFrame
    """
    # Criando uma nova coluna com a porcentagem
    dataframe[nome_col] = (dataframe[num_doc_esp]/total_por_UF)*100
    
    # Retorna o dataframe
    return dataframe

def cria_base_ordem_crescente(dataframe : pd.DataFrame, index_to_unstack: str ,col_porcentagem: str):
    """ Função que ordena os dados em ordem crescente, por UF, da menor soma de porcentagem até a maior

    :param pd.DataFrame dataframe: O dataframe o qual queremos ordenar
    :param str index_to_unstack: O multindex que será descompactado para formar uma nova coluna
    :param str col_porcentagem: A coluna a qual será a base da sua ordenação

    :return: O dataframe com os estados em ordem crescente da coluna que você especificou
    :rtype: pd.DataFrame

    """
    # desempacotando o dataframe com base no index especificado
    dataframe = dataframe.unstack(index_to_unstack)[col_porcentagem]

    # Somando as porcentagens do dataframe
    sum_percentage = dataframe.sum(axis=1)

    # Ordenando a lista do menor valor para o maior valor
    dataframe = dataframe.loc[sum_percentage.sort_values(ascending=True).index]

    # Retornando o Dataframe
    return dataframe

#####################################################################
# making each plot
def formata_cada_plot(dataframe: pd.DataFrame, title: str, numberplot: int, axis: np.ndarray) -> None:
    """Função para formatar cada plot com o mesmo estilo

    :param pd.DataFrame dataframe: O dataframe o qual queremos extrair os dados
    :param str title: O título que queremos colocar no gráfico
    :param int numberplot: Número do plot no gridplot
    :param np.ndarray axis: O nd.array com o gridplot

    :rype: None

    """

    # Criando o plot
    dataframe.plot(kind="bar", stacked=True, ax=axis[numberplot])

    # Colocando o título do gráfico
    axis[numberplot].set_title(title)

    # Formatando o eixo y para exibir a porcentagem
    axis[numberplot].yaxis.set_major_formatter(mtick.PercentFormatter())
    
    # Deixando todos os eixos com o limite superior de 60%
    axis[numberplot].set_ylim(0, 60)

    # Setando os parâmetros
    axis[numberplot].tick_params(axis='x', rotation=0, labelsize = 7)

    # Colocando os nomes nos eixos
    axis[numberplot].set_xlabel("Unidade Federativa")
    axis[numberplot].set_ylabel("Porcentagem")

# if __name__ == "__main__":
#     doctest.testmod()