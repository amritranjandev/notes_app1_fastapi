from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DB_URL = "sqlite:///./todos.db?check_same_thread=False"

engine = create_engine(url=SQLALCHEMY_DB_URL,
                       #    connect_args={
                       #    "check_same_therad": False}
                       )

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()
