import dataclasses
import json
from typing import List
from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config
from database.faqdata import FaqsData


router = APIRouter()


@router.get("/faqs/filtered_faqs/{search_phrase}")
def get_filtered_faqs(search_phrase: str, state: str = 'ALL', district: str = 'ALL'):
    faqsData = FaqsData()
    results = faqsData.full_text_search(search_phrase)
    return {'faqs' : results}

@router.get("/faqs/get_faqs/")
def get_faqs(state: str = 'ALL', district: str = 'ALL'):
    faqsData = FaqsData()
    results = faqsData.get_all_faqs()
    return {'faqs' : results}