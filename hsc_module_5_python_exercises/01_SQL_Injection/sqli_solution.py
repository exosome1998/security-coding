import sqlite3
db = sqlite3.connect(":memory:")
cur = db.cursor()
user_input = "hacker' OR '1'='1"

# Line 1: Use '?' placeholder
query = "SELECT * FROM users WHERE username = ?"

# Line 2: Execute safely
cur.execute(query, (user_input,))
print("Query executed safely.")