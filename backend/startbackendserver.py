from fastapi import FastAPI
import uvicorn

from api import phonenumbers
from api import districtcasenumbers
from api import districtinfos

app = FastAPI()
app.include_router(phonenumbers.router)
app.include_router(districtcasenumbers.router)
app.include_router(districtinfos.router)

uvicorn.run(app, port=8000)
