import dataclasses
import json
from typing import List
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

    # with sqlite3.connect(config.DATABASE_PATH) as connection:
    #    c = connection.cursor()
    #    c.execute("""
    #                SELECT name
    #                FROM Districts""")
    #    result = [r[0] for r in c.fetchall()]
    #    connection.close
    return {'district_names': district_names,
            'district_states': district_states}


@router.get("/district_infos/{district_name}")
def get_districts(district_name: str):
    spreadsheet = GoogleSpreadSheetCrawler()
    district_infos = spreadsheet.crawl_spreadsheet('1PYKjc5Kvk1ErUx3aqTGb7Czw5UYYeENUWoV6TZOaQls', 'Kreise!A2:F404')
    matching_row = None
    for row in district_infos:
        if row[0] == district_name:
            matching_row = row
    return {'district_state': matching_row[1],
            'citizien_hotline': matching_row[2],
            'test_hotline': matching_row[3],
            'info_web_page': matching_row[4],
            'best_practice': matching_row[5]}


@dataclasses.dataclass
class Question:
    district: str
    question: str
    answer: str


@router.get("/help/{district_name}")
def get_questions(district_name: str):
    spreadsheet = GoogleSpreadSheetCrawler()
    questions_raw = spreadsheet.crawl_spreadsheet('1UpKyRQVA5wW32wSkW0xajl5rvxJ28Ogmgazt5xIGX10', 'Fragen!A2:D')
    questions: List[Question] = [Question(info[0], info[2], info[3]) for info in questions_raw]
    only_for_district: List[Question] = [question for question in questions if question.district == district_name]
    return [question for question in only_for_district]
