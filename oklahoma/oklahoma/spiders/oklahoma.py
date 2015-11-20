import scrapy

class OklahomaFinanceSpider(scrapy.Spider):
    name = "OklahomaFinanceSpider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://data.ok.gov/dataset/revolving-funds-october-2014"
            ]

    def parse(self, response): 

        name = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"panel-pane pane-node")]/h2/text()').extract()
        description = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"field-item even")]/p/text()').extract()
        csv_link = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[0].extract()
        xml_link = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[1].extract()
        json_link = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[2].extract()
        rdf_link = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[3].extract()
        
        print name, description, csv_link, xml_link, json_link, rdf_link