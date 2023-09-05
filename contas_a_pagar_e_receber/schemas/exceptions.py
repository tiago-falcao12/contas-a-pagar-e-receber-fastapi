class NotFound(Exception):
    def __init__(self, name: str):
        self.name = name


class MyException(Exception):
    def __init__(self, mensagem: str, status: int):
        self.mensagem = mensagem
        self.status = status
