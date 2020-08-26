"""
Este script ejemplifica como se debe usar el módulo tweet_links

Si se corre en ipython todo debe funcionar bien.

Por el momento no se pueden usar en jupyterlab la funcion
tweet_links.url_2_BeautifulSoup, ya que produce el error:
'RuntimeError: Cannot use HTMLSession within an existing event loop. Use AsyncHTMLSession instead.'
"""

import tweet_links as tl

# Ejemplos de url de artículos para obtener su contenido (notar que nexos producirá error):
aristegi="https://aristeguinoticias.com/0208/mexico/detienen-a-el-marro-lider-del-cartel-de-santa-rosa-de-lima/"
laJornada="https://www.jornada.com.mx/2020/08/02/mundo/023n1mun"
forbesMX="https://www.forbes.com.mx/capturan-a-el-marro-lider-del-cartel-santa-rosa-de-lima-en-celaya/"
nexos="https://www.nexos.com.mx/?p=49085"

# Para leer un artículo se usa tl.url_2_BeautifulSoup:
bs=tl.url_2_BeautifulSoup(aristegi)