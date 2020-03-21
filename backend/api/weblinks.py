from fastapi import APIRouter

router = APIRouter()

#DATA
WEBSITES_MENTAL_HEALTH = [
    {"name": "Telefonseelsorge online", "link": "idk"},
    {"name": "Noch iwas", "link": "idk"},
    ]
WEBSITES_CORONA_TESTING = [
    {"name": "Charite Fragebogen", "link": "covapp.charite.de/questionaire"},
    {"name": "Noch iwas", "link": "idk"},
    ]
WEBSITES_CORONA_INFECTED = [
    {"name": "informationen?", "link": "idk"},
    {"name": "Noch iwas", "link": "idk"},
    ]

@router.get("/weblinks/mentalhealth")
def get_websites():
    return {"websites": WEBSITES_MENTAL_HEALTH}

@router.get("/weblinks/coronatesting")
def get_websites():
    return {"websites": WEBSITES_CORONA_TESTING}

@router.get("/weblinks/coronainfected")
def get_websites():
    return {"websites": WEBSITES_CORONA_INFECTED}