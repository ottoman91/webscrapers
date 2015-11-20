import scrapy 
from oklahoma.items import OklahomaItem

class OklahomaFinanceSpider(scrapy.Spider):
    name = "OklahomaFinanceSpider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://data.ok.gov/dataset/revolving-funds-october-2014"
            ]

    def parse(self, response):  

        item = OklahomaItem()

        item['name'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"panel-pane pane-node")]/h2/text()').extract()
        item['description'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"field-item even")]/p/text()').extract()
        item['csv_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[0].extract()
        item['xml_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[1].extract()
        item['json_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[2].extract()
        item['rdf_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[3].extract()
        
        yield item
