import scrapy
from database.databaseconnection import DatabaseConnection
from database.faqdata import FaqsData, FaqItem
import re
import datetime

class GeneralFaqSaxonyAnhaltSpider(scrapy.Spider):
    name = 'general_faq_saxony_anhalt'
    start_urls = [
        'https://ms.sachsen-anhalt.de/themen/gesundheit/aktuell/coronavirus/faq/',
    ]

    def parse(self, response):
        faqsData = FaqsData()
        questions_with_answers = response.css('#c233373 li')
        for i in range(len(questions_with_answers)):
            question = questions_with_answers[i].css('strong::text').get()
            answer = re.search(r'<br>(.*)</li>', questions_with_answers[i].css('li').get()).group(1)
            faqsData.create_or_update_question(FaqItem('ALL', 'Sachsen-Anhalt', question, answer, ''))

class SchoolFaqSaxonyAnhaltSpider(scrapy.Spider):
    name = 'school_faq_saxony_anhalt'
    start_urls = [
        'https://mb.sachsen-anhalt.de/service/faq-coronavirus-covid-19/',
    ]

    def parse(self, response):
        faqsData = FaqsData()
        questions_with_answers = response.xpath('//body').re(r'<h2>.*?.</h2>.*?<a.*?Zum Seitenanfang</a>')
        for i in range(len(questions_with_answers)):
            question = re.search(r'<h2>(.*?.)</h2>', questions_with_answers[i]).group(1)
            answer = re.search(r'<h2>.*?.</h2>(.*?)<a.*?Zum Seitenanfang</a>', questions_with_answers[i]).group(1)
            faqsData.create_or_update_question(FaqItem('ALL', 'Sachsen-Anhalt', question, answer, '#Schule'))
