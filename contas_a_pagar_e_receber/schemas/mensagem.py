from pydantic import BaseModel


class Mensagem(BaseModel):
    resultado: str
