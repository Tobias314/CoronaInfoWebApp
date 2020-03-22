from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from api import phonenumbers
from api import districtcasenumbers
from api import districtinfos
from api import weblinks
from api import faqs

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
app.include_router(weblinks.router)
app.include_router(faqs.router)

if __name__ == "__main__":
    uvicorn.run(app)
