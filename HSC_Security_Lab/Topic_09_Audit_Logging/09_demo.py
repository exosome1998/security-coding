import time
with open("log.txt", "a") as f: # 'a' appends to file
    f.write(f"{time.ctime()}: Event
") # Write time + event
