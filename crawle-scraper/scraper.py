import scrapy


class CrawleSpider(scrapy.Spider):
    name = "crawle_spider"
    start_urls = ['http://brickset.com/sets/year-2019']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for crawle in response.css(SET_SELECTOR):


            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': crawle.css(NAME_SELECTOR).extract_first(),
                'pieces': crawle.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': crawle.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': crawle.css(IMAGE_SELECTOR).extract_first(),
            }
