import hashlib
# Demo: Hashing text into a secure hex string
hashed = hashlib.sha256("pass123".encode()).hexdigest()
print(f"Hashed: {hashed}")