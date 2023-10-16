import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import doctest

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

if __name__ == "__main__":
    doctest.testfile("../doctests.txt", verbose=True)