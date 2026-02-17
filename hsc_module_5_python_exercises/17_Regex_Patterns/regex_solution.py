import re
pwd = "Password"
found = bool(re.search("@", pwd))
if not found: print("Missing @")