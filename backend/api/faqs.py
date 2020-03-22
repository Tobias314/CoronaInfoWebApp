import dataclasses
import json
from typing import List
from fastapi import APIRouter
from datetime import datetime
import sqlite3
import config
from database.faqdata import FaqsData
from api.districtinfos import get_state_for_district


router = APIRouter()


@router.get("/faqs/filter_faqs/")
def get_filtered_faqs(search_phrase: str, district: str = None):
    faqsData = FaqsData()
    if search_phrase:
        if(district is not None):
            state = get_state_for_district(district)
        else:
            state=None
        results = faqsData.full_text_search(search_phrase, state) #TODO: also use district for search if we have better data
        return {'faqs' : results}
    else:
        return get_faqs(district)

@router.get("/faqs/get_faqs/")
def get_faqs(district: str = None):
    state = None
    if (district is not None):
        state = get_state_for_district(district)
    faqsData = FaqsData()
    results = faqsData.get_all_faqs(state)
    return {'faqs' : results}