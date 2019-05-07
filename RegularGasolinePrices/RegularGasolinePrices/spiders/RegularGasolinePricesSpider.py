# -*- coding: utf-8 -*-
import scrapy
from RegularGasolinePrices.items import GasolinePriceItem


class GasolinePricesSpider(scrapy.Spider):
    name = 'gasolineprices'
    # allowed_domains = ['www.eia.gov']

    def start_requests(self):
        urls = [
            'https://www.eia.gov/petroleum/gasdiesel/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # domain = 'https://www.eia.gov'

        # table rows for States
        table_rows = response.xpath('//div[@class="more"]/table[@class="simpletable"]/tr')[2:11]
        # get available release date
        released_date = response.xpath('//div[@class="more"]/table[@class="simpletable"]/tr')[1]

        for table_row in table_rows:

            item = GasolinePriceItem()
            item['State'] = table_row.xpath('td/a/text()').extract()[0]
            item['Released_Date'] = released_date.xpath('td/b/text()').extract()[2]
            item['Price'] = table_row.xpath('td/text()').extract()[3]

            yield item
