from pydantic import BaseModel, Field


class RequestFornecedorCliente(BaseModel):
    nome: str = Field(min_length=2, max_length=255)


class ResponseFornecedorCliente(RequestFornecedorCliente):
    id: int

    class Config:
        orm_mode = True
