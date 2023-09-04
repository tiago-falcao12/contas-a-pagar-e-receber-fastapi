from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

from contas_a_pagar_e_receber.config import (POSTGRES_DB,
                                             POSTGRES_HOST,
                                             POSTGRES_USER,
                                             POSTGRES_PASSWORD)


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        logger.info("[+] CONECTOU SESSÃO DATABASE")

        yield db
    finally:
        logger.info("[+] SESSÃO DATABASE FINALIZADA")
        db.close()
