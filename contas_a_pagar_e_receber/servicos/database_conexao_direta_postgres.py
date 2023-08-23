import psycopg2
from loguru import logger

from contas_a_pagar_e_receber.config import (POSTGRES_DB,
                                             POSTGRES_HOST,
                                             POSTGRES_USER,
                                             POSTGRES_PASSWORD,
                                             POSTGRES_PORT)


class ContasDataBase:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect_to_database(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=POSTGRES_DB,
                host=POSTGRES_HOST,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                port=POSTGRES_PORT
            )
            self.__cursor = self.__connection.cursor()
            logger.info("[+] Conexão estabelecida com o banco de dados.")
        except psycopg2.Error as erro:
            logger.error(
                f"[-] ERRO AO CONECTAR-SE COM O BANCO DE DADOS - {erro}")

    def close___connection(self):
        if self.__connection:
            self.__connection.close()
            logger.info("[+] Conexão com o banco de dados fechada.")
        if self.__cursor:
            self.__cursor.close()

    def get_contas(self, query: str):
        dados = []
        try:
            self.connect_to_database()
            self.__cursor.execute(query)
            dados = self.__cursor.fetchall()
            logger.debug(dados)
        except Exception as erro:
            logger.error(str(erro))
        return dados

    def __del__(self):
        self.close___connection()


if __name__ == "__main__":

    query = 'SELECT * FROM contas_pagar_e_receber'

    logger.info(ContasDataBase().get_contas(query))
