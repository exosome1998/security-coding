import sqlite3 # Import DB library
user_id = "101' OR '1'='1" # Malicious input simulation
# We use '?' placeholders so the DB treats input as text, not commands
print(f"Safe: Use '?' placeholders, don't add {user_id} directly.") # Explanation
