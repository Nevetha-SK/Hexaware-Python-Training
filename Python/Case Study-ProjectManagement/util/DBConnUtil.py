# util/DBConnUtil.py

import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            conn_str = PropertyUtil.get_property_string()
            return pyodbc.connect(conn_str)
        except Exception as e:
            print("DB connection error:", e)
            return None
