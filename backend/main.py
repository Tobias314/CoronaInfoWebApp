from fastapi import FastAPI
import uvicorn

from api import phonenumbers

app = FastAPI()
app.include_router(phonenumbers.router)

uvicorn.run(app, port=8000)
