import scrapy
from database.databaseconnection import DatabaseConnection
import re
import datetime

class GeneralFaqSaxonyAnhaltSpider(scrapy.Spider):
    name = 'general_faq_saxony_anhalt'
    start_urls = [
        'https://ms.sachsen-anhalt.de/themen/gesundheit/aktuell/coronavirus/faq/',
    ]

    def parse(self, response):
        self.dbc = DatabaseConnection()
        questions_with_answers = response.css('#c233373 li')
        c = self.dbc.cursor()
        for i in range(len(questions_with_answers)):
            question = questions_with_answers[i].css('strong::text').get()
            answer = re.search(r'<br>(.*)</li>', questions_with_answers[i].css('li').get()).group(1)

            c.execute("""
                        REPLACE INTO Faqs
                        VALUES ('ALL','Sachsen-Anhalt',?,?,'')
                        """, (question, answer))
        self.dbc.commit()

class SchoolFaqSaxonyAnhaltSpider(scrapy.Spider):
    name = 'school_faq_saxony_anhalt'
    start_urls = [
        'https://mb.sachsen-anhalt.de/service/faq-coronavirus-covid-19/',
    ]

    def parse(self, response):
        self.dbc = DatabaseConnection()
        questions_with_answers = response.xpath('//body').re(r'<h2>.*?.</h2>.*?<a.*?Zum Seitenanfang</a>')
        c = self.dbc.cursor()
        for i in range(len(questions_with_answers)):
            question = re.search(r'<h2>(.*?.)</h2>', questions_with_answers[i]).group(1)
            answer = re.search(r'<h2>.*?.</h2>(.*?)<a.*?Zum Seitenanfang</a>', questions_with_answers[i]).group(1)

            c.execute("""
                        REPLACE INTO Faqs
                        VALUES ('ALL','Sachsen-Anhalt',?,?,'#Schule')
                        """, (question, answer))
        self.dbc.commit()
