"""
Funciones para analizar artículos publicados
en twitter por diferentes periódicos.

Dependencias:
    - BeautifulSoup
    - requests_html 
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
    Lee una url con HTMLSession y retorna un BeautifulSoup
    """
    session = HTMLSession()
    r=session.get(url)
    return BeautifulSoup(r.html.html,features="lxml")

"""
async def __render_and_read_url(url):
    'Lee una url con AsyncHTMLSession, renderiza y retorna un BeautifulSoup'
    asession = AsyncHTMLSession()
    r=await asession.get(url)
    await r.html.arender(sleep=10,keep_page=True,scrolldown=5)
    soup = BeautifulSoup(r.html.html)
    return soup
"""

def __render_and_read_url(url):
    """
    Lee una url con AsyncHTMLSession, renderiza y retorna un BeautifulSoup
    """
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    soup = BeautifulSoup(r.html.html)
    return soup

async def main(url):
    await asyncio.gather(__render_and_read_url(url))

__is_websites_asynch={
    "aristeguinoticias.com": True,
    "www.jornada.com.mx": False,
    "www.forbes.com.mx": True}

__websites_2_readFunctions={
    "aristeguinoticias.com": __render_and_read_url,
    "www.jornada.com.mx": __read_url,
    "www.forbes.com.mx": __render_and_read_url}


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
    #read_function= __websites_2_readFunctions[website]
    if(__is_websites_asynch[website]):
        result=__render_and_read_url(url)
        """
        # python V < 3.8
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(main(url))
        loop.close()
        """
        """
        # python V 3.8
        asyncio.run(main(url))
        """
    else:
        result=__read_url(url)
    return result
#    return read_function(url)