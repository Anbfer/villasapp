import sqlite3
import logging

class SQLiteConnector:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        logging.info(f"Conectado ao banco de dados em: {database}")

    def execute(self, query, params=None):
        try:
            logging.info(f"Executando query: {query} | Params: {params}")
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            logging.info("Query executada com sucesso")
        except sqlite3.Error as e:
            logging.error(f"Erro ao executar a query: {e}")
            raise

    def fetchall(self):
        try:
            results = self.cursor.fetchall()
            logging.info(f"Resultados obtidos: {results}")
            return results
        except sqlite3.Error as e:
            logging.error(f"Erro ao obter resultados: {e}")
            raise

    def close(self):
        try:
            self.connection.close()
            logging.info("Conexão com o banco de dados fechada")
        except sqlite3.Error as e:
            logging.error(f"Erro ao fechar a conexão: {e}")
            raise

    def create_tables(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS moradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            senha TEXT NOT NULL
        );
        """
        self.execute(create_table_query)