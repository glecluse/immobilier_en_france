import sqlite3
import os

class Database:
    def __init__(self):
        db_path = os.path.abspath("project.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query: str, params: tuple = ()):
        return self.cursor.execute(query, params)

    def commit(self):
        self.conn.commit()
        self.conn.close()