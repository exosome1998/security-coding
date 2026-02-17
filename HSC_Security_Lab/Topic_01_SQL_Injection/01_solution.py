import sqlite3
db = sqlite3.connect(":memory:") # Create temp DB in RAM
cur = db.cursor() # Create cursor tool
user_input = "hacker' OR '1'='1" # Malicious input
query = "SELECT * FROM users WHERE username = ?" # '?' tells DB this is data only
cur.execute(query, (user_input,)) # Input is bound safely as a tuple
