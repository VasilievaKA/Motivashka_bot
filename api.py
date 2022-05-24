import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

USER_NAME = os.getenv("USER_NAME", "user")
USER_PASS = os.getenv("USER_PASS", "password")
DB_HOST = '127.0.0.1'
DB_NAME = "db"
engine = create_engine(url=f'mysql+pymysql://root:12345@127.0.0.1:3306/db?charset=utf8')

app = FastAPI()
connection = engine.connect()
table_name = 'quotes'
keys = ['id_quotes', 'id', 'quote']
session = Session(bind=engine)


@app.get("/")
async def root(theme_id: int = None):
    if theme_id is None:
        comand = f'SELECT id_quotes, quote FROM quotes'
    else:
        comand = f'SELECT quote FROM quotes WHERE id={theme_id} ORDER BY rand() LIMIT 1'
    result = connection.execute(comand)
    return result.all()


@app.put("/")
async def root(id: int, theme_id: int, quote: str):
    try:
        connection.execute("INSERT INTO quotes (id_quotes, id, quote) VALUES (%s, %s, '%s')" % (id, theme_id, quote))
    except IntegrityError:
        return "Такой темы нет"
    comand = f'SELECT id_quotes, quote FROM quotes'
    result = connection.execute(comand)
    return result.all()