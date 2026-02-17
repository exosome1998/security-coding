import hashlib
user_pwd = "AdminPassword" # Plain text password
h_obj = hashlib.sha256(user_pwd.encode()) # Convert to bytes & hash
final = h_obj.hexdigest() # Get readable hex string
print(f"Secure Hash: {final}") # Print the fingerprint
