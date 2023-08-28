from pydantic import BaseModel, Field
from typing import List

from enum import Enum


class TipoEnum(str, Enum):
    PAGAR = "PAGAR"
    RECEBER = "RECEBER"


class ContasRequest(BaseModel):
    descricao: str = Field(min_length=5, max_length=50)
    valor: float = Field(gt=0)
    tipo: TipoEnum


class ContasResponse(ContasRequest):
    id: int

    class Config:
        orm_mode = True


class ListContasResponse(BaseModel):
    resultado: List[ContasResponse]
