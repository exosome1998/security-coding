import os # Import the OS library to interact with the file system

def fetch_image_vulnerable(filename): # Function to fetch an image
    path = "stories/" + filename # PROBLEM: Blindly adding user text to the path string
    print(f"--- LOG --- Attempting to open: {path}") # Show the resulting dangerous path
    return "Image Data" # Return fake image content

# HACK TEST: Attacker uses '../' to leave the stories folder and see secrets
fetch_image_vulnerable("../private_server_config.txt") # Run the hack
