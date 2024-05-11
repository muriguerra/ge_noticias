import scrapy


class GeSpider(scrapy.Spider):
    name = "ge"
    allowed_domains = ["ge.globo.com"]
    start_urls = ["https://ge.globo.com/esports/"]

    def parse(self, response, **kwargs):
        links_noticias = response.css("a.feed-post-link::Attr('href')").getall()
        for link in links_noticias:
            yield scrapy.Request(link, callback=self.parse_noticia, cb_kwargs={
                'link': link
            })

    def parse_noticia(self, response, **kwargs):
        yield {
            'autor': response.css('.content-publication-data__from::text').get(),
            'titulo': response.css('.content-head__title::text').get(),
            'subtitulo': response.css('.content-head__subtitle::text').get(),
            'link': kwargs['link'],
            'publicacao': response.css('.content-publication-data__updated > time::text').get()

        }







 #def parse_noticia(self, response, **kwargs):
       # for noticia in response.xpath('//div[@class="_evg"]/div[@class="_evt"]/div[@class="bastian-feed-item"]'):
           # yield {
         #       'titulo': noticia.css(".feed-post-link p::text").get(),
          #      'link': noticia.css("a.feed-post-link::Attr('href')").get()
          #  }