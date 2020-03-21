from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config

from database.databaseconnection import DatabaseConnection

router = APIRouter()

@router.get("/district_case_number/{district_name}")
def read_district_case_number(district_name: str):
    with sqlite3.connect(config.DATABASE_PATH) as connection:
        c = connection.cursor()
        c.execute("""
                    SELECT case_number, data_time_stamp
                    FROM DistrictCaseNumbers
                    WHERE district_name=?
                    ORDER BY data_time_stamp DESC""",
                  (district_name,))
        result = c.fetchone()
        connection.close()
    return {'case_number' : int(result[0]),
            'data_time_stamp' : datetime.fromtimestamp(int(result[1]))}

