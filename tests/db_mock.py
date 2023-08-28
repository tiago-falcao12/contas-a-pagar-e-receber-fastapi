from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from contas_a_pagar_e_receber.servicos.database import Base, get_db
from contas_a_pagar_e_receber import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./teste_db.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        return db
    finally:
        db.close()


def create_db_test():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db
