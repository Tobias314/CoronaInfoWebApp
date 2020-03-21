from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config

from database.databaseconnection import DatabaseConnection

router = APIRouter()

@router.get("/district_infos/get_districts")
def get_districts():
    with sqlite3.connect(config.DATABASE_PATH) as connection:
        c = connection.cursor()
        c.execute("""
                    SELECT name
                    FROM Districts""")
        result = [r[0] for r in c.fetchall()]
        connection.close
    return {'district_names' : result}

