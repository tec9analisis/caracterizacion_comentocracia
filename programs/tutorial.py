"""
|------------------------------------------------------------------|
| tutorial.py                                                      |
| tecn9                                                            |
| https://github.com/tec9analisis/caracterizacion_comentocracia    |
|------------------------------------------------------------------|

Este script ejemplifica como se debe usar el módulo tweet_links

Si se corre en ipython todo debe funcionar bien.

Por el momento NO SE PUEDE USAR EN JUPYTERLAB LA FUNCIÓN
TWEER_LINKS.RUL_2_BEAUTIFULSOUP, ya que produce el error:
'RuntimeError: Cannot use HTMLSession within an existing
event loop. Use AsyncHTMLSession instead.'

De preferenica CIERRA PESTAÑAS QUE ALENTEN TU CONEXIÓN a internet
como youtube, etc.
"""

import tweet_links as tl

# Ejemplos de url de artículos para obtener su contenido (notar que nexos producirá error):
#------------------------------------------------------------------------------------------

aristegi="https://aristeguinoticias.com/0208/mexico/detienen-a-el-marro-lider-del-cartel-de-santa-rosa-de-lima/"
laJornada="https://www.jornada.com.mx/2020/08/02/mundo/023n1mun"
forbesMX="https://www.forbes.com.mx/capturan-a-el-marro-lider-del-cartel-santa-rosa-de-lima-en-celaya/"
nexos="https://www.nexos.com.mx/?p=49085"

# Para leer un artículo se usa tl.url_2_BeautifulSoup:
#-----------------------------------------------------

print("obteniendo contenido de '{}'...".format(laJornada))

bs_jornada=tl.url_2_BeautifulSoup(laJornada)

print("\tdone!\n")
print("obteniendo contenido de '{}'...".format(aristegi))

bs_aristegi=tl.url_2_BeautifulSoup(aristegi)

print("\tdone!\n")
print("obteniendo contenido de '{}'...".format(forbesMX))

bs_forbes=tl.url_2_BeautifulSoup(forbesMX)

print("\tdone!\n")

######################################################################
#                                                                    #
#    Haciendo webscrapping para obtener contenido:                   #
#                                                                    #
#    el código de abajo hace webscraping para los                    #
#    tres sitios que tenemos.                                        #
#                                                                    #
#    - Convertir a función                                           #
#                                                                    #
#    - usar beautifullSoup en lugar de strings (si es conveniente)   #
#      para quitar las tags dentro del texto                         #
#                                                                    #
######################################################################

# Ejemplo de webscrapping para la jornada
#-----------------------------------------------------

print("webscrapping '{}'".format(aristegi))
jornada_text=bs_jornada.article.find_all("div",id="article-text")[0].find_all("p")
print("\tdone!\n")

# Ejemplo de webscraping para coontenido de aristegi noticias
#-----------------------------------------------------

print("webscrapping '{}'".format(laJornada))
content=list()
queue=bs_aristegi.find_all("div")
while(len(queue)>0):
    tag=queue.pop(0)
    for son in tag.find_all("div"):
        tag.append(son)
    if("class" in tag.attrs):
        if("wrappercont" in tag["class"]):
            content.append(tag)
aristegi_text=content[0]
print("\tdone!\n")

# Ejemplo de webscrapping para forbes
#-----------------------------------------------------

print("webscrapping '{}'".format(forbesMX))
content=list()
queue=bs_forbes.find_all("div")
while(len(queue)>0):
    tag=queue.pop(0)
    for son in tag.find_all("div"):
        tag.append(son)
    if("class" in tag.attrs):
        if("entry-content" in tag["class"]):
            content.append(tag)
forbes_text=content[0]
print("\tdone!\n")

print("\n\t".join(["puedes acceder al contenido de los stios en las variables:","jornada_text","aristegi_text","forbes_text"]))