import sqlite3 # Import library to manage the database
db = sqlite3.connect(":memory:") # Setup temporary database in memory
cur = db.cursor() # Setup the cursor for command execution
cur.execute("CREATE TABLE followers (handle TEXT, count INTEGER)") # Create a table for social stats
cur.execute("INSERT INTO followers VALUES ('Influencer', 5000), ('NewUser', 10)") # Add sample data

def get_followers_safely(handle_input):
    # STEP 1: Use '?' as a placeholder. This tells the DB that data is coming, not code.
    query = "SELECT count FROM followers WHERE handle = ?" # TODO: Set this string properly
    
    # STEP 2: Pass 'handle_input' inside a tuple (data,) as the second argument
    # Instruction: result = cur.execute(query, (handle_input,)).fetchone()
    result = None # TODO: Write the secure execution line here
    
    return result # Return the single safe result found
