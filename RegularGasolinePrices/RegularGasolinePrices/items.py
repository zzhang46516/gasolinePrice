from scrapy import Item, Field


class GasolinePriceItem(Item):

    State = Field()
    Released_Date = Field()
    Price = Field()
