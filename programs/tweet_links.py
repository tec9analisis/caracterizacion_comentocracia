"""
Funciones para obtener el contendio de diferentes sitios web (revisar atributos)

NOTA: url_2_BeautifulSoup no puede ser llamada desde jupyter lab.

Atributos:

    - websites: Lista de sitios web que se pueden procesar
    
Funciones:
(para una descripción detallada ver docstring the las funciones)

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

    - __websites_2_readFunctions: Diccionario que mapea los sitios web a funciones de lectura

Funciones privadas:

    - __read_url
    - __read_and_render_url
"""

from bs4 import BeautifulSoup
from requests_html import HTMLSession, AsyncHTMLSession
import errors
import asyncio

websites=["aristeguinoticias.com",
          "www.jornada.com.mx",
          "www.forbes.com.mx"]

def __read_url(url):
    """
    Retorna el contenido de la url obtenido con HTMLSession.
    """
    session = HTMLSession()
    return session.get(url)

def __read_and_render_url(url):
    """
    Retorna el contenido de la url obtenido y renderizado con HTMLSession.
    """
    r=__read_url(url)
    r.html.render()
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