import json
user = {"name": "Bob"} # Data dict
out = json.dumps(user) # Auto-escape chars
print(f"Safe: {out}") # Print safe string
