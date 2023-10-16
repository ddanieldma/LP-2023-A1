import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import doctest

def ler_csv(caminho_csv) -> pd.DataFrame: 
    """Recebe um arquivo csv e retona um dataframe

    :param str caminho_csv: caminho do arquivo csv

    :return: DataFrame produzido com base no arquivo csv
    :rtype: pandas.DataFrame

    Exemplo:
    >>> df = ler_csv("../bases_de_dados/dados_teste.csv")
    >>> df.head()
       Estado    DDD
    0  MG        32
    1  RJ        21
    2  SP        11

    >>> ler_csv('arquivo_fake.csv')
    'Arquivo não encontrado'
    """
    try:
        df = pd.read_csv(caminho_csv, encoding='latin-1', sep = ';')
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except ValueError:
        return "O caminho deve ser uma string"
    else:
        return df    

print(ler_csv("../bases_de_dados/dados_teste.csv"))


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

    >>> removing_list_columns(df, ["DF", "RS", "SC"])
    'O nome da coluna não está no dataframe'

    >>> removing_list_columns(df, "DF")
    'Você não colocou uma lista de strings'

    """

    try:
        # Checando se é uma lista
        if not isinstance(lista, list):
            raise ValueError
        
        # Checando se todos os elementos da lista são strings
        for nome_coluna in lista:
            if not isinstance(nome_coluna, str):
                raise ValueError
            
        # Tira as colunas do Dataframe
        dataframe.drop(lista, axis=1, inplace=True)

    except KeyError as error:
        return "O nome da coluna não está no dataframe"
    except ValueError:
        return "Você não colocou uma lista de strings"
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

    >>> df = pd.DataFrame(dados)
    >>> removing_columns_from_to(df, "DF", "RJ")
    'A coluna informada não existe no dataframe'

    >>> df2 = ["SP", "RS", "SC", "RJ"]
    >>> removing_columns_from_to(df2, "SP", "RS")
    "Houve um erro. Por favor, tente novamente:'list' object has no attribute 'columns'"
    >>> 
    """
    try:
        # Verificando se a coluna é uma string
        if not isinstance(start_col, str) or not isinstance(end_col, str):
            raise ValueError    
        
        # Pegando o índice das colunas que queremos retirar
        beginning_col = dataframe.columns.get_loc(start_col)
        finish_col = dataframe.columns.get_loc(end_col)

        # Caso o usuário tenha colocado as colunas ao contrário
        if finish_col < beginning_col:
            beginning_col = finish_col
            finish_col = dataframe.columns.get_loc(start_col)
        
        # Selecionando o nome das colunas para retirar
        cols_to_drop = dataframe.columns[beginning_col:finish_col+1]

        dataframe.drop(cols_to_drop, axis=1, inplace=True)
    except KeyError:
        return "A coluna informada não existe no dataframe"
    except ValueError:
        return "O nome da coluna informada não é uma string"
    except Exception as error:
        return f"Houve um erro. Por favor, tente novamente:{error}"
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
    Exemplo:
    >>> dados = {"Universidade": ["UFRJ", "FGV", "PUC"], "TP_CATEGORIA_ADMINISTRATIVA": [1, 5, 6]}
    >>> df = pd.DataFrame(dados)
    >>> df = type_of_university(df)
    >>> df
      Universidade  TP_CATEGORIA_ADMINISTRATIVA Tipo de Universidade
    0         UFRJ                            1              Pública
    1          FGV                            5              Privada
    2          PUC                            6              Privada

    >>> type_of_university(df, "TP")
    'O nome da coluna não existe ou não é uma string'
    """
    try: 
        # Dicionário com o tipo de escola
        types_of_universities = {1: "Pública", 2:"Pública", 3: "Pública", 4: "Privada", 5:"Privada", 6:"Privada", 7: "Privada", 8: "Privada", 9: "Privada"}
        
        # Adicionando a nova coluna
        dataframe[nome_coluna_nova] = dataframe[column].map(types_of_universities)

    except KeyError:
        return "O nome da coluna não existe ou não é uma string"
    except Exception as error:
        return f"Houve um erro. Por favor, tente novamente:{error}"
    else:
        # Retorna o dataframe
        return dataframe

######################################################################################
# Análise
def cria_porcentagem(dataframe: pd.DataFrame, nome_col: str, num_doc_esp: str, total_por_UF: pd.DataFrame):
    """ Cria uma coluna porcentagem com base em outras colunas do dataframe

    :param pd.DataFrame dataframe: O dataframe do qual se deseja adicionar a coluna com a porcentagem
    :param str nome_col: O nome da coluna que queremos adicionar
    :param str num_doc_esp: O nome da coluna a qual desejamos saber a porcentagem
    :param pd.DataFrame total_por_UF: Dataframe com o total de docentes por UF

    :return: O dataframe com uma coluna a mais com a a porcentagem devida
    :rtype: pd.DataFrame

    >>> dados = {'QT_DOC_TOTAL': {('AC', 'Privada'): 339, ('AC', 'Pública'): 1002, ('AL', 'Privada'): 2370, ('AL', 'Pública'): 2690, ('AM', 'Privada'): 2088}, 'QT_DOC_EX_DOUT': {('AC', 'Privada'): 70, ('AC', 'Pública'): 522, ('AL', 'Privada'): 553, ('AL', 'Pública'): 1622, ('AM', 'Privada'): 427}}
    >>> df = pd.DataFrame(dados)
    >>> df = df.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
    >>> total_doc_por_UF = total_doc_por_UF = df.groupby(level='SG_UF_IES')['QT_DOC_TOTAL'].sum()
    
    >>> cria_porcentagem(df, "PCT_DOC_TOT", "nome_aleatorio", total_doc_por_UF)
    'O nome da coluna não existe'

    >>> cria_porcentagem(df, "PCT_DOC_TOT", 3, total_doc_por_UF)
    'O nome da coluna não é uma string'
    """
    try:
        # Checando se é uma string
        if not isinstance(nome_col, str) or not isinstance(num_doc_esp, str):
            raise ValueError

        
        # Criando uma nova coluna com a porcentagem
        dataframe[nome_col] = (dataframe[num_doc_esp]/total_por_UF)*100

    except KeyError:
        return "O nome da coluna não existe"
    except ValueError:
        return "O nome da coluna não é uma string"
    except Exception as error:
        return f"Houve um erro. Por favor, tente novamente:{error}"
    # Retorna o dataframe
    return dataframe




def cria_base_ordem_crescente(dataframe : pd.DataFrame, index_to_unstack: str ,col_porcentagem: str):
    """ Função que ordena os dados em ordem crescente, por UF, da menor soma de porcentagem até a maior

    :param pd.DataFrame dataframe: O dataframe o qual queremos ordenar
    :param str index_to_unstack: O multindex que será descompactado para formar uma nova coluna
    :param str col_porcentagem: A coluna a qual será a base da sua ordenação

    :return: O dataframe com os estados em ordem crescente da coluna que você especificou
    :rtype: pd.DataFrame
    >>> dados = {'PCT_DOUT_TOTAL': {('AC', 'Privada'): 5.219985085756898, ('AC', 'Pública'): 38.92617449664429, ('AL', 'Privada'): 10.928853754940711, ('AL', 'Pública'): 32.055335968379445, ('AM', 'Privada'): 7.8463800073502386}}
    >>> df = pd.DataFrame(dados)
    >>> df = df.rename_axis(["SG_UF_IES", "Tipo de Universidade"])
    

    >>> cria_base_ordem_crescente(df, "Tipo de Universidade", "qualquer_nome")
    'O nome do index ou da coluna não existe no dataframe'

    >>> cria_base_ordem_crescente(df, 1, 4)
    'O(s) nome(s) da(s) coluna(s) que você passou não é uma string'

    """
    try: 
        # Checando se é uma string
        if not isinstance(index_to_unstack, str) or not isinstance(col_porcentagem, str):
            raise ValueError
        # desempacotando o dataframe com base no index especificado
        dataframe = dataframe.unstack(index_to_unstack)[col_porcentagem]

        # Somando as porcentagens do dataframe
        sum_percentage = dataframe.sum(axis=1)

        # Ordenando a lista do menor valor para o maior valor
        dataframe = dataframe.loc[sum_percentage.sort_values(ascending=True).index]

    except KeyError:
        return "O nome do index ou da coluna não existe no dataframe"
    except ValueError:
        return "O(s) nome(s) da(s) coluna(s) que você passou não é uma string"
    except Exception as error:
        return f"Houve um erro. Por favor, tente novamente:{error}"
    else:
        # Retornando o Dataframe
        return dataframe
    
# if __name__ == "__main__":
#     doctest.testmod()
