import sqlite3

# Demo: Parameterized queries prevent SQL Injection
user_id = "101' OR '1'='1"
print(f"Safe Method: Use '?' placeholders instead of inserting {user_id} directly.")