import time
with open("security.txt", "a") as f: # Open in append mode
    f.write(f"{time.ctime()} - FAIL
") # Log timestamped error
