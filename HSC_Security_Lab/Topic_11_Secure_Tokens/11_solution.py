import secrets
my_token = secrets.token_hex(8) # Generate 8 secure bytes
print(f"Token: {my_token}") # Print hex string
