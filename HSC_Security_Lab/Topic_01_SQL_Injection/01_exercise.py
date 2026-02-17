import sqlite3
db = sqlite3.connect(":memory:")
cur = db.cursor()
user_input = "hacker' OR '1'='1"

# TASK: Prevent SQL Injection by using a placeholder (?)
# BAD EXAMPLE: query = "SELECT * FROM users WHERE username = " + user_input

# TODO: Create a variable 'query' that uses a '?' instead of the user_input variable

# TODO: Run cur.execute() passing the query and the user_input as a tuple (user_input,)
