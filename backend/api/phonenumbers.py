from fastapi import APIRouter

router = APIRouter()

#DATA
PHONE_NUMBERS_HEALTH_DEPARTMENT = {'Potsdam' : "0815"}

@router.get("/phone_number/health_department/{city_name}")
def read_item(city_name: str):
    return {"phone_number": PHONE_NUMBERS_HEALTH_DEPARTMENT[city_name]}

@router.get("/phone_number/mentalhealth")
def get_numbers():
    return {"phone_numbers": [
                {"name": "Telefonseelsorge", "number": "0800-1110111 / 116123"},
                {"name": "Kinder- und Jugendtelefon", "number": "0800-116111"},
                {"name": "Elterntelefon", "number": "0800-1110550"},
                {"name": "Hilfetelefon Häusliche Gewalt", "number": "0800-0116016"},
                {"name": "Hilfetelefon Sexueller Missbrauch", "number": "0800-2255530"},
                {"name": "Beratungsstelle des Lesben- und Schwulenverbandes", "number": "0721-8317953"},
    ]}