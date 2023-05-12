import sqlite3

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple=None, fetchone=False,  fetchall=None, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
        id NOT NULL,
        lang_code varchar(255) NOT NULL
        )
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, lang_code: str):
        sql = "INSERT INTO Users (id, lang_code) VALUES (?, ?)"
        parameters = (id, lang_code)
        self.execute(sql, parameters=parameters, commit=True)

    def set_lang(self, id: int, lang_code: str):
        sql = "UPDATE Users SET lang_code = ? WHERE id = ?"
        parameters = (lang_code, id)
        self.execute(sql, parameters=parameters, commit=True)

    def get_lang(self, id):
        sql = "SELECT lang_code FROM Users WHERE id = ?"
        parameters = (id,)
        return self.execute(sql, parameters=parameters, commit=True, fetchone=True)


def logger(statement):
    print(f"""
    ___________________________________________
    Executing {statement}
    ___________________________________________""")