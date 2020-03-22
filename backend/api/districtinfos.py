import dataclasses
from typing import List
from fastapi import APIRouter
from webcrawler.googlespreadsheet.googlespreadhsheetcrawler import GoogleSpreadSheetCrawler

router = APIRouter()
QUESTION_SHEET = "1UpKyRQVA5wW32wSkW0xajl5rvxJ28Ogmgazt5xIGX10"
DISTRICT_SHEET = '1PYKjc5Kvk1ErUx3aqTGb7Czw5UYYeENUWoV6TZOaQls'


@router.get("/district_infos/get_districts")
def get_districts():
    spreadsheet = GoogleSpreadSheetCrawler()
    district_infos = spreadsheet.crawl_spreadsheet(DISTRICT_SHEET, 'Kreise!A2:B404')
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
    district_infos = spreadsheet.crawl_spreadsheet(DISTRICT_SHEET, 'Kreise!A2:F404')
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
    questions_raw = spreadsheet.crawl_spreadsheet(QUESTION_SHEET, 'Fragen!A2:D')
    questions: List[Question] = [Question(info[0], info[2], info[3]) for info in questions_raw]
    only_for_district: List[Question] = [question for question in questions if question.district == district_name]
    return [question for question in only_for_district]


@router.post("/help/{district_name}")
def post_question(district_name: str, question: str):
    values: List[List[str]] = [[district_name, "", question, ""]]
    crawler = GoogleSpreadSheetCrawler()
    crawler.post_data(QUESTION_SHEET, "Fragen!A2:D", values)


@dataclasses.dataclass
class StateInfo:
    state: str
    max_number_public: str
    club_sport_allowed: bool
    website: str
    is_lockdown: bool



@router.get("/lockdown_info/{district_name}")
def get_public_measures_info(district_name: str):
    state_of_district: str = get_state_for_district(district_name)
    crawler = GoogleSpreadSheetCrawler()
    states_raw = crawler.crawl_spreadsheet(DISTRICT_SHEET, "Bundeslaender!A2:E")
    states_raw = [state for state in states_raw if len(state) == 5]
    states: List[StateInfo] = [StateInfo(state[0], state[1], state[2] == "ja", state[3], state[4] == "ja") for state in states_raw]
    info_for_requested_state: StateInfo = next(filter(lambda state_info: state_info.state == state_of_district, states))
    return info_for_requested_state






def get_state_for_district(district_name: str) -> str:
    crawler = GoogleSpreadSheetCrawler()
    districts = crawler.crawl_spreadsheet(DISTRICT_SHEET, "Kreise!A2:B")
    district: List[str] = next(filter(lambda district: district[0] == district_name, districts))
    return district[1]
