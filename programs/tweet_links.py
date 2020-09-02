"""
|------------------------------------------------------------------|
| tweet_links.py                                                   |
| tecn9                                                            |
| https://github.com/tec9analisis/caracterizacion_comentocracia    |
|------------------------------------------------------------------|

Funciones para obtener el contendio de diferentes sitios web (revisar atributos)

NOTAS:

    - url_2_BeautifulSoup no puede ser llamada desde jupyter lab.

    - Para renderizar un sitio web en la función __read_and_render_url usa:
      r.html.render(sleep=10,keep_page=True,scrolldown=5)
      sin embargo puede que los parámetros necesarios varíen dependiendo
      de la velocidad de tu conección a internet.
      De preferencia CIERRA PESTAÑAS QUE ALENTEN TU CONEXIÓN como youtube, etc.

Atributos:

    - websites:
      Lista de sitios web que se pueden procesar
    
Funciones:
(para una descripción detallada ver docstring de las funciones)

    - url_2_BeautifulSoup:
      Dado un url, retorna un BeautifulSoup
      si el sitio está en 'websites'
      o error.

Dependencias:

    - BeautifulSoup:
      Se usa para procesar el contenido html.

    - requests_html:
      Se usa para obtener el contenido de las url.

    - errors:
      Módulo donde se definen los errores que pueden aparecer.

Atributos privados:

    - __websites_2_readFunctions:
      Diccionario que mapea los sitios web a funciones de lectura

Funciones privadas:

    - __read_url
    - __read_and_render_url
"""

from bs4 import BeautifulSoup
import requests_html as rhtml
import errors
import asyncio

websites=["aristeguinoticias.com",
          "www.jornada.com.mx",
          "www.forbes.com.mx"]

def __read_url(url):
    """
    Retorna el contenido de la url obtenido con HTMLSession.
    """
    session = rhtml.HTMLSession()
    return session.get(url)

def __read_and_render_url(url,timeout=16,sleep=10,keep_page=True,scrolldown=5):
    """
    Retorna el contenido de la url obtenido y renderizado con HTMLSession.

    A escepción de timeout, todos los parámetros predefinidos se usan siempre.

    timeout solo se usa si huvo un error por conecciónde a internet.
    """
    r=__read_url(url)
    try:
        r.html.render(sleep=sleep,keep_page=keep_page,scrolldown=scrolldown)
    except rhtml.MaxRetries as e:
        print("\tRender error:'{}'\n\tNow re-trying with 'timeout={}'".format(e,timeout))
        r.html.render(timeout=timeout,sleep=sleep,keep_page=keep_page,scrolldown=scrolldown)
    except:
        raise
    return r

__websites_2_readFunctions={
    "aristeguinoticias.com": __read_and_render_url,
    "www.jornada.com.mx": __read_url,
    "www.forbes.com.mx": __read_and_render_url}


def url_2_BeautifulSoup(url):
    """
    Dado un url, retorna un BeautifulSoup
    si el sitio está en 'websites'
    o error.

    Input:
        - url (str)

    Output:
        - (BeautifulSoup object)
        - website (str)

    Error:
        - errors.Non_Avalible_Site

    pipeline:
        - Revisa si las funciones que tenemos sirven
            para el sitio de la url.
        - Renderiza el sitio si es necesario (toma mas tiempo).
    """
    website=url.split("/")[2]
    if(website not in websites):
        raise errors.Not_Avalible_Site(website)
    read_function= __websites_2_readFunctions[website]
    r=read_function(url)
    return BeautifulSoup(r.html.html,features="lxml")