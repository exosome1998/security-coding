import sqlite3 # Import the sqlite3 library to handle all database operations

db = sqlite3.connect(":memory:") # Create a database in RAM that resets every time the script stops
cur = db.cursor() # Create a cursor object which acts like a pen to write SQL commands

cur.execute("CREATE TABLE users (handle TEXT, email TEXT)") # Define a table to store handles and emails
cur.execute("INSERT INTO users VALUES ('GamerGirl', 'gg@mail.com')") # Insert first sample user record
cur.execute("INSERT INTO users VALUES ('Secret_Admin', 'admin@site.com')") # Insert second sample user record

def search_vulnerable(user_input):
    # THE PROBLEM: The f-string {} merges user input directly into the SQL command logic
    query = f"SELECT email FROM users WHERE handle = '{user_input}'" 
    print(f"--- LOG --- The Database is running: {query}") # Print the command so students see the hack
    return cur.execute(query).fetchall() # Run the query and return every matching piece of data found

# HACK TEST: The input "' OR '1'='1" tricks the database into thinking the condition is always True
print(f"HACKED RESULT: {search_vulnerable(\"' OR '1'='1\")}")
