from mcp.server.fastmcp import FastMCP
from typing import Optional
from query_exec import execute_db_query
from sqdb import create_mock_db


create_mock_db()

app=FastMCP(name="Server for Db queries")


@app.tool()
def get_revenue_summary(start_date : Optional[str] = None ,end_date: Optional[str] = None ,plan: Optional[str] = None):
    """
    Returns total revenue within optional date range and optional plan filter.
    """

    query = """
        SELECT SUM(o.amount)
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        WHERE o.status = 'Completed'
    """
    params = []

    if start_date:
        query += " AND o.order_date >= ?"
        params.append(start_date)

    if end_date:
        query += " AND o.order_date <= ?"
        params.append(end_date)

    if plan:
        query += " AND c.plan = ?"
        params.append(plan)

    result=execute_db_query(query,params)
    
    return {
        "total_revenue": result or 0,
        "start_date": start_date,
        "end_date": end_date,
        "plan": plan
    }

@app.resource("info://server")
def server_info() -> str:
    info={
        "name": "Getting revenue directly querying the database as chat",
        "version": "1.0.0",
        "author": "Ashutosh Goswami"
    }


@app.tool()
def query_db(sql: str) -> str:
    """Run a query against the mock SQLite database."""
    # Your sqlite code here
    return "Result"

if __name__ == "__main__":
    app.run(transport="http",host="0.0.0.0", port=8000)