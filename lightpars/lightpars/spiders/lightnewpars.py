import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/petrozavodsk/category/svet",
                  "https://www.divan.ru/petrozavodsk/category/svet/page-2",
                  "https://www.divan.ru/petrozavodsk/category/svet/page-3",
                  "https://www.divan.ru/petrozavodsk/category/svet/page-4",
                  "https://www.divan.ru/petrozavodsk/category/svet/page-5",
                  "https://www.divan.ru/petrozavodsk/category/svet/page-6"]

    def parse(self, response):
        lightings = response.css('div.WdR1o')
        for lighting in lightings:
            yield {
                'name' : lighting.css('div.lsooF span::text').get(),
                'price' : lighting.css('div.q5Uds span::text').get(),
                'url' : lighting.css('a').attrib['href']
            }
