from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os
from fastapi import FastAPI
from sqlalchemy.sql.expression import func

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DataBase = declarative_base()


class Quotes(DataBase):
    __tablename__ = "quotes"
    id_quotes = Column(Integer, primary_key=True)
    id = Column(Integer, ForeignKey('names.id'), nullable=False)
    quote = Column(String(255), unique=True, nullable=False)


class Names(DataBase):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


class QuoteGet(BaseModel):
    id: int


class QuoteCreate(QuoteGet):
    id_quotes: int
    quote: str


class NamesGet(BaseModel):
    id: int


class NamesCreate(NamesGet):
    name: str


def create_quote(db: Session, new_quote: QuoteCreate):
    db_ = Quotes(**new_quote.dict())
    db.add(db_)
    db.commit()
    db.refresh(db_)
    return


def get_quote(db: Session):
    return db.query(Quotes).all()


def get_by_id(db: Session, id: int):
    return db.query(Quotes).filter(Quotes.id == id).order_by(func.random()).limit(1).all()


def get_by_name(db: Session, quote: str):
    return db.query(Quotes).filter(Quotes.quote == quote).all()


def delete_quote_by_id(db: Session, id: int):
    _ = db.query(Quotes).filter(Quotes.id == id).delete()
    db.commit()
    return


def create_name(db: Session, new_name: NamesGet):
    db_ = Names(**new_name.dict())
    db.add(db_)
    db.commit()
    db.refresh(db_)
    return


def get_names(db: Session):
    return db.query(Names).all()


def get_name_by_id(db: Session, id: int):
    return db.query(Names).filter(Names.id == id).limit(1).all()


def get_name_by_name(db: Session, name: str):
    return db.query(Names).filter(Names.name == name).all()


def delete_name_by_id(db: Session, id: int):
    _ = db.query(Names).filter(Names.id == id).delete()
    db.commit()
    return


app = FastAPI()


@app.on_event("startup")
async def startup():
    DataBase.metadata.create_all(bind=engine)


@app.get("/get quote")
async def root(theme_id: int = None):
    with Session(engine) as db:
        if theme_id is None:
            return get_quote(db)
        else:
            return get_by_id(db, theme_id)


@app.get("/get name")
async def root(id: int = None):
    with Session(engine) as db:
        if id is None:
            return get_names(db)
        else:
            return get_name_by_id(db, id)


@app.post("/add quote")
async def root(theme_id: int, quote: str):
    with Session(engine) as db:
        quote_id = db.query(Quotes).count()+1
        res = get_by_name(db, quote)
        if not res:
            new_quote = QuoteCreate(
                id_quotes=quote_id,
                id=theme_id,
                quote=quote
            )
            create_quote(db=db, new_quote=new_quote)
            return db.query(Quotes).order_by(Quotes.id_quotes)[-1]
        else:
            return "Такая цитата уже есть"


@app.post("/add name")
async def root(new_id: int, topic: str):
    with Session(engine) as db:
        res = get_name_by_id(db, new_id)
        res1 = get_name_by_name(db, topic)
        if not res and not res1:
            new_name = NamesCreate(
                id=new_id,
                name=topic
            )
            create_name(db=db, new_name=new_name)
            return get_names(db)
        else:
            return "Такая тема уже есть"
