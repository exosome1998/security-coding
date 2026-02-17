import time
with open("security.txt", "a") as f:
    f.write(f"{time.ctime()} - ALERT: Fail\n")