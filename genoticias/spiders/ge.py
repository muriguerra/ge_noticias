import scrapy
from ..items import GenoticiasItem


class GeSpider(scrapy.Spider):
    name = "ge"
    allowed_domains = ["ge.globo.com"]
    start_urls = ["https://ge.globo.com/esports/"]
    pagina = 2

    def parse(self, response, **kwargs):
        links_noticias = response.css("a.feed-post-link::Attr('href')").getall()
        for link in links_noticias:
            yield scrapy.Request(link, callback=self.parse_noticia, cb_kwargs={
                'link': link
            })

        proxima_pagina = 'https://ge.globo.com/esports/index/feed/pagina-' + str(GeSpider.pagina) + '.ghtml'
        if GeSpider.pagina <= 5:
            GeSpider.pagina += 1
            yield scrapy.Request(proxima_pagina, callback=self.parse)



    def parse_noticia(self, response, **kwargs):
        items = GenoticiasItem()

        items['autor'] = response.css('.content-publication-data__from::text').get()
        items['titulo'] = response.css('.content-head__title::text').get()
        items['subtitulo'] = response.css('.content-head__subtitle::text').get()
        items['link'] = kwargs['link']
        items['publicacao'] = response.css('.content-publication-data__updated > time::text').get()

        yield items
