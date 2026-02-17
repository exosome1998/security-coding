try:
    val = int("abc") # This will crash
except ValueError: # Catch specific error
    print("Conversion failed.") # Graceful exit
