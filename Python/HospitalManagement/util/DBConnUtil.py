import pyodbc
from util.DBPropertyUtil import getPropertyString

def getConnection(file='db.properties'):
    try:
        conn_str = getPropertyString(file)
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print("❌ DB connection failed:", e)
        return None
