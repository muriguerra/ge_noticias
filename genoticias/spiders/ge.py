from typing import Union

import pandas as pd
import scrapy
from scrapy import Spider
from twisted.internet.defer import Deferred

from ..items import GenoticiasItem


class GeSpider(scrapy.Spider):
    name = "ge"
    allowed_domains = ["ge.globo.com"]
    start_urls = ["https://ge.globo.com/esports/"]
    pagina = 2

    def parse(self, response, **kwargs):
        # Extrai os links de todas as notícias na página inicial
        links_noticias = response.css("a.feed-post-link::Attr('href')").getall()
        # Itera sobre os links das notícias e faz uma requisição para cada uma delas
        for link in links_noticias:
            yield scrapy.Request(link, callback=self.parse_noticia, cb_kwargs={
                'link': link
            })
        # Constrói a URL da próxima página com base no número da página
        proxima_pagina = 'https://ge.globo.com/esports/index/feed/pagina-' + str(GeSpider.pagina) + '.ghtml'
        # Verifica se a próxima página está dentro do limite (neste caso, 10 páginas)
        if GeSpider.pagina <= 10:
            GeSpider.pagina += 1
            yield scrapy.Request(proxima_pagina, callback=self.parse)



    def parse_noticia(self, response, **kwargs):
        items = GenoticiasItem()
        # Extrai as informações da notícia e atribui aos campos do item
        autor = response.css('.content-publication-data__from::text').get()
        if "Por" in autor:
            autor = autor.replace("Por", "", 1).strip()  # Remove "Por" e espaços extras
        if "," in autor:
            autor = autor.split(",")[0].strip()  # Pega o que está antes da ","
        items['autor'] = autor
        items['titulo'] = response.css('.content-head__title::text').get()
        items['subtitulo'] = response.css('.content-head__subtitle::text').get()
        items['link'] = kwargs['link']
        items['publicacao'] = response.css('.content-publication-data__updated > time::text').get()

        yield items
