from fastapi import FastAPI
from db.database import test_db_connection
app = FastAPI()


@app. on_event("startup")
def on_startup():
    test_db_connection

@app.get("/")
def read_root():
    return {
        "Message": "hello world"
        }