from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, Union
from datetime import date

from enum import Enum

from contas_a_pagar_e_receber.schemas.fornecedor_cliente import ResponseFornecedorCliente

class TipoEnum(str, Enum):
    PAGAR = "PAGAR"
    RECEBER = "RECEBER"


class ContasBody(BaseModel):
    descricao: str = Field(min_length=5, max_length=50)
    valor: float = Field(gt=0)
    tipo: TipoEnum
    data_previsao: date


class ContasRequest(ContasBody):
    fornecedor_cliente_id: Optional[int]


class ContasResponse(ContasBody):
    id: int
    fornecedor: Union[ResponseFornecedorCliente, None]

    class Config:
        orm_mode = True


class ContasReponseBaixa(ContasResponse):
    data_baixa: Optional[date]
    valor_baixa: Optional[float]
    baixado: Optional[bool]


class ListContasResponse(BaseModel):
    resultado: List[ContasResponse]
