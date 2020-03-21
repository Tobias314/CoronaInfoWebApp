from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api import phonenumbers
from api import districtcasenumbers
from api import districtinfos

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(phonenumbers.router)
app.include_router(districtcasenumbers.router)
app.include_router(districtinfos.router)

uvicorn.run(app, port=8000)