social_db = {"Influencer_X": "MySecretPassword123", "Admin": "AdminPass77"} # PROBLEM: Storing passwords in 'Plain Text'

def leak_database(): # Function to simulate a hacker reading the database
    print("--- LOG --- Database Breach! Passwords exposed:") # Alert that data is being stolen
    for user, pwd in social_db.items(): # Loop through every user in the database
        print(f"User: {user} | Password: {pwd}") # Show the hacker exactly what the user typed

leak_database() # Run the simulation to show how easy it is to read stolen data
