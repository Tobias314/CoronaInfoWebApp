import dataclasses
import json
from typing import List
from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config
from database.faqdata import FaqsData


router = APIRouter()


@router.get("/faqs/filter_faqs/")
def get_filtered_faqs(search_phrase: str, state: str = 'ALL', district: str = 'ALL'):
    faqsData = FaqsData()
    if search_phrase:
        results = faqsData.full_text_search(search_phrase)
        return {'faqs' : results}
    else:
        return get_faqs(state, district)

@router.get("/faqs/get_faqs/")
def get_faqs(state: str = 'ALL', district: str = 'ALL'):
    faqsData = FaqsData()
    results = faqsData.get_all_faqs()
    return {'faqs' : results}