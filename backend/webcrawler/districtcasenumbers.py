import scrapy
from database.databaseconnection import DatabaseConnection
import re
import datetime

class DistrictCaseNumbersSaxonyAnhaltSpider(scrapy.Spider):
    name = 'district_case_numbers_saxony_anhalt'
    start_urls = [
        'https://verbraucherschutz.sachsen-anhalt.de/hygiene/infektionsschutz/infektionskrankheiten/coronavirus/',
    ]

    def parse(self, response):
        self.dbc = DatabaseConnection()
        time_string = response.css('#c234506 p:nth-child(2)::text').get()
        reg = re.search(r'(\d+)\.(\d+)\.(\d{4}).*\((\d+)\:(\d+)', time_string)
        date = datetime.datetime(int(reg.group(3)),int(reg.group(2)),int(reg.group(1)),int(reg.group(4)),int(reg.group(5)))
        case_numbers = response.css('td:nth-child(2)')
        districts = response.css('td:nth-child(1)')
        c = self.dbc.cursor()
        for i in range(14):
            district_name = districts[i].css('::text').get()[3:]
            case_number = int(case_numbers[i].css('::text').get())

            c.execute("""
                        INSERT INTO DistrictCaseNumbers
                        SELECT ?,?,?,?
                        WHERE NOT EXISTS (SELECT 1 
                                            FROM DistrictCaseNumbers 
                                            WHERE district_name=? AND source_url=?)
                        """, (district_name, self.start_urls[0], case_number, int(date.timestamp()), district_name, self.start_urls[0]))
        self.dbc.commit()