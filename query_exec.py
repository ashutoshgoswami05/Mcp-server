
import sqlite3
import os
import libsql
from dotenv import load_dotenv

load_dotenv()

def execute_db_query(query,params):
    try:
        url = os.getenv("DB_URL")
        auth_token = os.getenv("DB_TOKEN")
        print("trying connection",auth_token,url)
        conn = libsql.connect("imported.db", sync_url=url, auth_token=auth_token)
        result=conn.execute(query,params).fetchall()
        return result
    except Exception as e:
         print("Exception occured ",e)
    