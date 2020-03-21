from fastapi import APIRouter

router = APIRouter()

#DATA
PHONE_NUMBERS_MENTAL_HEALTH = [
    {"name": "Telefonseelsorge", "number": "0800-1110111 / 116123"},
    {"name": "Kinder- und Jugendtelefon", "number": "0800-116111"},
    {"name": "Elterntelefon", "number": "0800-1110550"},
    {"name": "Hilfetelefon Häusliche Gewalt", "number": "0800-0116016"},
    {"name": "Hilfetelefon Sexueller Missbrauch", "number": "0800-2255530"},
    {"name": "Beratungsstelle des Lesben- und Schwulenverbandes", "number": "0721-8317953"},
    ]

@router.get("/phone_number/mentalhealth")
def get_numbers():
    return {"phone_numbers": PHONE_NUMBERS_MENTAL_HEALTH}