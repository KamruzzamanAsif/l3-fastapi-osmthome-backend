import pyodbc

from ..config import FABRIC_PWD, FABRIC_UID
from .config import AUTH_METHOD, DATABASE, DATABASE_SERVER_URL


def get_database_connection():
    try:
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={DATABASE_SERVER_URL};"
            f"DATABASE={DATABASE};"
            f"Authentication={AUTH_METHOD};"
            f"UID={FABRIC_UID};"
            f"PWD={FABRIC_PWD};"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        raise Exception("Database connection error:", e)
