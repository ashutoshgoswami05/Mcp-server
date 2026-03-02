import sqlite3

def create_mock_db():
    conn = sqlite3.connect('company_vitals.db')
    cursor = conn.cursor()

    # 1. Create Tables
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            plan TEXT, -- 'Free', 'Pro', 'Enterprise'
            signup_date DATE
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            amount REAL,
            status TEXT, -- 'Completed', 'Pending', 'Refunded'
            order_date DATE,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );

        CREATE TABLE IF NOT EXISTS support_tickets (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            issue_category TEXT,
            priority TEXT, -- 'Low', 'High', 'Urgent'
            is_resolved BOOLEAN,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
    ''')

    # 2. Insert Mock Data
    customers = [
        (1, 'TechCorp Solutions', 'admin@techcorp.com', 'Enterprise', '2023-01-15'),
        (2, 'Sarah Jenkins', 'sarah.j@gmail.com', 'Free', '2023-05-20'),
        (3, 'Global Logistics Inc', 'billing@globallog.com', 'Enterprise', '2022-11-10'),
        (4, 'Kevin Zhang', 'kevinz@startup.io', 'Pro', '2024-02-01')
    ]
    
    orders = [
        (101, 1, 2500.00, 'Completed', '2024-01-10'),
        (102, 3, 5000.00, 'Completed', '2024-01-12'),
        (103, 2, 0.00, 'Completed', '2024-01-15'),
        (104, 4, 150.00, 'Pending', '2024-02-05'),
        (105, 1, 2500.00, 'Completed', '2024-02-10')
    ]

    tickets = [
        (1, 1, 'Billing Inquiry', 'Low', 1),
        (2, 3, 'API Downtime', 'Urgent', 0),
        (3, 4, 'Feature Request', 'Medium', 1)
    ]

    cursor.executemany('INSERT OR IGNORE INTO customers VALUES (?,?,?,?,?)', customers)
    cursor.executemany('INSERT OR IGNORE INTO orders VALUES (?,?,?,?,?)', orders)
    cursor.executemany('INSERT OR IGNORE INTO support_tickets VALUES (?,?,?,?,?)', tickets)

    conn.commit()
    conn.close()
    print("Database 'company_vitals.db' created successfully!")

if __name__ == "__main__":
    create_mock_db()