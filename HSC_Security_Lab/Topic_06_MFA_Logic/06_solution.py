pwd = "ok"
pin = 1 # Wrong pin
auth = (pwd == "ok") and (pin == 5) # Checks both conditions
print(f"Access Result: {auth}") # False
