
import sqlite3

def execute_db_query(query,params):
    conn = sqlite3.connect('company_vitals.db')
    cursor = conn.cursor()
    cursor.execute(query,params)
    result=cursor.fetchone()[0]

    print(result)

    conn.close()

    return result
    