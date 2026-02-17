import re
pwd = "Password" # Weak password
if not re.search("@", pwd): # Check pattern
    print("Weak: Needs '@'") # Enforce rule
