
## Realizar un web Scrapping con la libreria Beutifuk Soup
## sitio scrapeado paraScrapear.com

import requests
from bs4 import BeautifulSoup

if "__main__" == __name__:
    page = requests.get("https://parascrapear.com/")
    soup = BeautifulSoup(page.text, "html.parser")
    buscar_bloque = soup.find_all("blockquote")
    for bloque in buscar_bloque:
        try:
            author = bloque.find(class_= "author").text
            categorias = bloque.find(class_= "cat").text
            frase = bloque.find('q')

            Texto_scrappeado = "{} \n -{} ({}) \n"

            print(Texto_scrappeado.format(frase, author, categorias))
        except:

            print()
