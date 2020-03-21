from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config
from webcrawler.googlespreadsheet.googlespreadhsheetcrawler import GoogleSpreadSheetCrawler

router = APIRouter()

@router.get("/district_infos/get_districts")
def get_districts():
    spreadsheet = GoogleSpreadSheetCrawler()
    district_infos = spreadsheet.crawl_spreadsheet('1PYKjc5Kvk1ErUx3aqTGb7Czw5UYYeENUWoV6TZOaQls', 'Kreise!A2:B404')
    district_names = [row[0] for row in district_infos]
    district_states = [row[1] for row in district_infos]

    #with sqlite3.connect(config.DATABASE_PATH) as connection:
    #    c = connection.cursor()
    #    c.execute("""
    #                SELECT name
    #                FROM Districts""")
    #    result = [r[0] for r in c.fetchall()]
    #    connection.close
    return {'district_names' : district_names,
            'district_states' : district_states}

@router.get("/district_infos/{district_name}")
def get_districts(district_name: str):
    spreadsheet = GoogleSpreadSheetCrawler()
    district_infos = spreadsheet.crawl_spreadsheet('1PYKjc5Kvk1ErUx3aqTGb7Czw5UYYeENUWoV6TZOaQls', 'Kreise!A2:F404')
    matching_row = None
    for row in district_infos:
        if row[0] == district_name:
            matching_row = row
    return {'district_state' : matching_row[1],
            'citizien_hotline' : matching_row[2],
            'test_hotline' : matching_row[3],
            'info_web_page' : matching_row[4],
            'best_practice' : matching_row[5]}

