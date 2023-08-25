from pydantic import BaseModel
from typing import List


class ContasRequest(BaseModel):
    descricao: str
    valor: float
    tipo: str


class ContasResponse(ContasRequest):
    id: int

    class Config:
        orm_mode = True


class ListContasResponse(BaseModel):
    resultado: List[ContasResponse]
