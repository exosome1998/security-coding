import time # Import the time library

def verify_secure(entered_code): # Secure function for 2FA
    # STEP 1: Capture the start time
    start_time = time.time() # TODO: Use time.time()
    
    # STEP 2: Compare the code to '9988'
    result = (entered_code == "9988") # TODO: Store the True/False result
    
    # STEP 3: Force the function to wait until 0.3 seconds has passed
    # Instruction: while time.time() - start_time < 0.3: pass
    pass # TODO: Add the while loop here
