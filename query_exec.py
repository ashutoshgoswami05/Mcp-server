
import sqlite3
import os
import libsql_client
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

URL = os.getenv("DB_URL")
TOKEN = os.getenv("DB_TOKEN")



def execute_db_query(query,params):
    with libsql_client.create_client_sync(url=URL, auth_token=TOKEN) as client:
            # 3. Execute the query
            # Turso's execute handles both the query and params
            result_set = client.execute(query, params or [])
            
            # 4. Handle the result
            # .rows returns a list of rows; we check if it's not empty
            if result_set.rows:
                result = result_set.rows[0][0]
                print(result)
                return result
            
            return None
    