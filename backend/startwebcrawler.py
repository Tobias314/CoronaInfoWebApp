import scrapy
from twisted.internet import reactor
from twisted.internet.task import deferLater
from scrapy.crawler import CrawlerProcess

import config
from webcrawler.districtcasenumbers import DistrictCaseNumbersSaxonyAnhaltSpider
from webcrawler.statefaqs import GeneralFaqSaxonyAnhaltSpider, SchoolFaqSaxonyAnhaltSpider

spiders = [GeneralFaqSaxonyAnhaltSpider, SchoolFaqSaxonyAnhaltSpider]

def sleep(self, *args, seconds):
    """Non blocking sleep callback"""
    return deferLater(reactor, seconds, lambda: None)

def crash(failure):
    print('oops, spider crashed')
    print(failure.getTraceback())

def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(lambda results: print('waiting {} seconds before restart...'.format(config.BETWEEN_CRAWLS_PAUSE)))
    deferred.addErrback(crash)
    deferred.addCallback(sleep, seconds=config.BETWEEN_CRAWLS_PAUSE)
    deferred.addCallback(_crawl, spider)
    return deferred


process = CrawlerProcess(settings={
    'DOWNLOAD_DELAY': config.CRAWLER_DOWNLOAD_DELAY
})

for spider in spiders:
    _crawl(None, spider)

process.start()