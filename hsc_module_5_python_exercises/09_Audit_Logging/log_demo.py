import time
with open("log.txt", "a") as f:
    f.write(f"{time.ctime()}: Login\n")