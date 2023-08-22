from decouple import config


POSTGRES_DB: str = config('POSTGRES_DB')
PORT_DB: int = config('PORT_DB')
POSTGRES_USER: str = config('POSTGRES_USER')
POSTGRES_PASSWORD: str = config('POSTGRES_PASSWORD')
