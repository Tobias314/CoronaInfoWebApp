from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config
from webcrawler.googlespreadsheet.googlespreadhsheetcrawler import GoogleSpreadSheetCrawler

from database.databaseconnection import DatabaseConnection

router = APIRouter()

@router.get("/district_case_number/{district_name}")
def read_district_case_number(district_name: str):
    #with sqlite3.connect(config.DATABASE_PATH) as connection:
    #    c = connection.cursor()
    #    c.execute("""
    #                SELECT case_number, data_time_stamp
    #                FROM DistrictCaseNumbers
    #                WHERE district_name=?
    #                ORDER BY data_time_stamp DESC""",
    #              (district_name,))
    #    result = c.fetchone()
    #    connection.close
    spreadsheet = GoogleSpreadSheetCrawler()
    all_data = spreadsheet.crawl_spreadsheet('1wg-s4_Lz2Stil6spQEYFdZaBEp8nWW26gVyfHqvcl8s', 'Haupt!A6:S406')
    matching_row = None
    for row in all_data:
        if row[0] == district_name:
            matching_row = row
    return {'type' : matching_row[1],
            'number_cases' : matching_row[3],
            'change_rate' : matching_row[4],
            'time' : matching_row[9]
            }
