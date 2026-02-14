import os # Import the OS library

def get_profile_pic(filename_input): # Secure function to get a profile picture
    # STEP 1: Use basename to strip away any directory slashes (/) or dots (..)
    safe_name = os.path.basename(filename_input) # TODO: Use os.path.basename()
    
    # STEP 2: Combine the folder name with the safe filename
    final_path = "profiles/" + safe_name # TODO: Set to "profiles/" + safe_name
    
    return final_path # Return the cleaned, safe path
