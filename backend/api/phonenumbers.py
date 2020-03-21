from fastapi import APIRouter

router = APIRouter()

#DATA
PHONE_NUMBERS_HEALTH_DEPARTMENT = {'Potsdam' : "0815"}

@router.get("/phone_number/health_department/{city_name}")
def read_item(city_name: str):
    return {"phone_number": PHONE_NUMBERS_HEALTH_DEPARTMENT[city_name]}
