from fastapi import FastAPI

app = FastAPI()

#DATA
PHONE_NUMBERS_GESUNDHEITSAMT = {'Potsdam' : "0815"}

@app.get("/phone_number/gesundheitsamt/{city_name}")
def read_item(city_name: str):
    return {"phone_number": PHONE_NUMBERS_GESUNDHEITSAMT[city_name]}