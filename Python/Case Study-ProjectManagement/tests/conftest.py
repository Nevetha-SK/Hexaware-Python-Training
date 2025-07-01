# tests/conftest.py
import pytest
from util.DBConnUtil import DBConnUtil

@pytest.fixture(scope='session')
def db_conn():
    """
    Provides a shared database connection for all tests.
    """
    conn = DBConnUtil.get_connection()
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def clean_db(db_conn):
    """
    Automatically cleans all tables before each test runs.
    """
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM Task")
    cursor.execute("DELETE FROM Employee")
    cursor.execute("DELETE FROM Project")
    db_conn.commit()
    cursor.close()
