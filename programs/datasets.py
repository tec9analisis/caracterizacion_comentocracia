"""
|------------------------------------------------------------------|
| datasets.py                                                   |
| tecn9                                                            |
| https://github.com/tec9analisis/caracterizacion_comentocracia    |
|------------------------------------------------------------------|

Funciones para acceder a bases de datos de diferentes fuentes.

Atributos:

    - None
    

Funciones:
(para una descripción detallada ver docstring de las funciones)

    - load_TASS:
      Dados los archivos TASS en la misma carpeta o el path hacia los archivos regresa un Dataframe de pandas.

Dependencias:

    - Pandas:
    Implementacion de base de datos para importación y manejo.


Atributos privados:

    - None

"""

import pandas as pd
pd.set_option('max_colwidth',1000)

def load_TASS(path=""):
    """
    Retorna pandas.DataFrame con base de datos TASS2019 de MX, ES, CR, PE, UY.
    
    """
    types = ['_train.csv','_dev.csv']
    countries = ['MX','ES','CR','PE','UY']

    c = [pd.read_csv(path+"TASS2019_country_"+ country + datatype, engine='python') for country in countries for datatype in types]
    tweets_corpus = pd.concat(c)

    tweets_corpus = tweets_corpus[["tweetid","content","value"]]

    tweets_corpus = tweets_corpus[tweets_corpus.value.isin(['P', 'N'])]
    tweets_corpus.insert(3, "polarity_bin", (tweets_corpus.value=='P').astype('int'), True)
    
    return tweets_corpus