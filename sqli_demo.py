import sqlite3 # Import the library to manage the SQL database

db = sqlite3.connect(":memory:") # Create a database in RAM (Memory) that is wiped when the script stops
cur = db.cursor() # Create a cursor object, which acts like a pen to write SQL commands to the DB

# 1. Setup the table for our "InstaClone" scenario
cur.execute("CREATE TABLE users (handle TEXT, email TEXT)") # Define a table with two text columns
cur.execute("INSERT INTO users VALUES ('GamerGirl', 'gg@mail.com')") # Add a sample user handle and email
cur.execute("INSERT INTO users VALUES ('Secret_Admin', 'admin@site.com')") # Add a second sample user

def search_vulnerable(user_input):
    # 2. THE PROBLEM: This line merges user text and SQL code together using an f-string
    # Because of the '{user_input}', the database cannot tell where the code ends and data begins
    query = f"SELECT email FROM users WHERE handle = '{user_input}'" 
    
    print(f"--- LOG --- The Database is running: {query}") # Display the final command so students see the hack
    return cur.execute(query).fetchall() # Execute the combined string and return every matching record

# 3. HACK TEST: We use single quotes outside so we can use double quotes inside WITHOUT backslashes
# The payload ' OR '1'='1' makes the database logic "True OR True", bypassing the username check
attack_payload = "' OR '1'='1" 
print(f"HACKED RESULT: {search_vulnerable(attack_payload)}") # Run the function with the malicious input
