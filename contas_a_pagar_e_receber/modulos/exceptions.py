from fastapi import Request
from loguru import logger
from fastapi.responses import JSONResponse

from contas_a_pagar_e_receber.schemas.exceptions import NotFound, MyException


async def not_found_exception_handler(request: Request, exc: NotFound):
    logger.error(f'[-] ERRO: {type(exc).__name__}')

    return JSONResponse(status_code=404, content={"message": f"Oops! {exc.name} inexistente!"})

async def my_exception_exception_handler(request: Request, exc: MyException):
    logger.error(f'{type(exc).__name__}')

    return JSONResponse(status_code=exc.status, content={"message": exc.mensagem})