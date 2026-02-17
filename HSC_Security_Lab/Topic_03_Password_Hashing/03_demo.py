import hashlib # Standard crypto lib
# sha256 turns text into a unique fingerprint
hashed = hashlib.sha256("pass123".encode()).hexdigest() # Hash the bytes
print(f"Hashed: {hashed}") # Prints secure hex string
