import pandas as pd
import numpy as np
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import doctest


def formata_cada_plot(dataframe: pd.DataFrame, title: str, numberplot: int, axis: np.ndarray) -> None:
    """Função para formatar cada plot com o mesmo estilo

    :param pd.DataFrame dataframe: O dataframe o qual queremos extrair os dados
    :param str title: O título que queremos colocar no gráfico
    :param int numberplot: Número do plot no gridplot
    :param np.ndarray axis: O nd.array com o gridplot

    :rype: None
    
    Exemplo 
    >>> axes = plt.subplots(1, 3, figsize=(15, 5))
    >>> data = pd.DataFrame({"RJ":[1,2,3]})

    >>> formata_cada_plot(data, "Hello", 15, axes)
    'O número do plot não existe'

    >>> formata_cada_plot(data, 1, 1, axes)
    'O título não é uma string'
    """
    try: 
        if not isinstance(title, str):
            raise ValueError
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
        axis[numberplot].set_ylabel("Porcentagem em relação ao total de docentes")

    except ValueError:
        return "O título não é uma string"
    except IndexError:
        return "O número do plot não existe"

if __name__ == "__main__":
    doctest.testmod()
