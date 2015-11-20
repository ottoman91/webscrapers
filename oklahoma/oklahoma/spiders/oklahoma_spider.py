import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from oklahoma.items import OklahomaItem

class OklahomaFinanceSpider(CrawlSpider):
    name = "OklahomaFinanceSpider"
    allowed_domains = ["data.ok.gov"]
    start_urls = [
			"http://data.ok.gov/browse?f[0]=bundle_name%3ADataset&f[1]=im_field_categories%3A4191"
            ] 

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//li[@class="pager-next"]',)), callback="parse_start_url", follow= True),
    ) 

    
    def parse_start_url(self, response): 

        for href in response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"search-results apachesolr_search-results")]/h3/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)  

        





    def parse_dir_contents(self, response):  

        item = OklahomaItem()

        item['name'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"panel-pane pane-node")]/h2/text()').extract()
        item['description'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"field-item even")]/p/text()').extract()
        item['csv_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[0].extract()
        #item['xml_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[1].extract()
        #item['json_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[2].extract()
        #item['rdf_link'] = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "),"btn btn-primary data-link")]/@href')[3].extract()
        
        yield item
