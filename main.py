## Realizar un web Scrapping con la libreria Beutifuk Soup
## sitio scrapeado paraScrapear.com

import requests
from bs4 import BeautifulSoup

page = requests.get("https://parascrapear.com/")
soup = BeautifulSoup(page.text, "html.parser")
buscar_bloque = soup.find_all("blockquote")
for bloque in buscar_bloque:
    author = bloque.find(class_= "author").text
    categorias = bloque.find(class_= "cat").text
    frase = bloque.find('q')
    print([author, categorias, frase])