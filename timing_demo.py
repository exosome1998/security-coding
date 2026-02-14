import time # Import time library to simulate or measure processing speed

def verify_vulnerable(code_input): # Function to check a 2FA code
    if code_input == "1234": # Check if the input matches the secret
        time.sleep(0.5) # PROBLEM: If correct, the computer "sleeps" (pauses), making it slow
        return True # Return success
    return False # FAILURE: Returns instantly (0.0s), which tells a hacker they were wrong fast

print("Testing wrong code... (Returns instantly)") # Inform the user
verify_vulnerable("0000") # Demonstrate the fast failure
