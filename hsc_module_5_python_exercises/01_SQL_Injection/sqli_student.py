import sqlite3
db = sqlite3.connect(":memory:")
cur = db.cursor()
user_input = "hacker' OR '1'='1"

# STEP 1: Replace the dangerous string concatenation with a '?' placeholder
# TODO: query = "SELECT * FROM users WHERE username = " + user_input 

# STEP 2: Pass user_input as a tuple in the execute function
# TODO: cur.execute(query, (...))