import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from crochet import setup
import logging

setup()  # Initialize Crochet

class RegulationSpider(scrapy.Spider):
    name = 'regulation_spider'

    def __init__(self, search_query=None, *args, **kwargs):
        super(RegulationSpider, self).__init__(*args, **kwargs)
        self.search_query = search_query
        self.start_urls = [
            'https://dataprotection.ie',
            'https://eur-lex.europa.eu/',
            'https://www.legislation.gov.uk/',
            # Add more URLs as needed
        ]

    def parse(self, response):
        # Logic to parse the response and extract data
        for post in response.css('div.news-post'):
            title = post.css('h2.title::text').get()
            logging.info(f'Found article: {title}')
            summary = post.css('p.summary::text').get()
            url = post.css('a::attr(href)').get()
            date = post.css('span.date::text').get()

            yield {
                'title': title,
                'summary': summary,
                'url': response.urljoin(url),
                'date': date,
            }


@defer.inlineCallbacks
def start_scraping(search_query):
    runner = CrawlerRunner()
    yield runner.crawl(RegulationSpider, search_query=search_query)
    reactor.stop()  # Stop the reactor when done
