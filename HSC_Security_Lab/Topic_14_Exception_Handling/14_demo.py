try:
    x = 1/0 # Crash
except ZeroDivisionError:
    print("Safe Error") # Handle crash
