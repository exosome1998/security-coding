import bcrypt # Import the library for cryptographic hashing
secure_db = {} # Setup an empty dictionary for secure storage

def signup_user(username, password):
    # STEP 1: Convert the string password to bytes
    password_bytes = password.encode('utf-8') # TODO: Use .encode('utf-8')
    
    # STEP 2: Generate a unique salt for this user
    salt = bcrypt.gensalt() # TODO: Use bcrypt.gensalt()
    
    # STEP 3: Hash the bytes and the salt together
    hashed = bcrypt.hashpw(password_bytes, salt) # TODO: Use bcrypt.hashpw()
    
    # STEP 4: Save the hash to secure_db[username]
    # secure_db[username] = hashed # Save the scrambled version only
    pass
