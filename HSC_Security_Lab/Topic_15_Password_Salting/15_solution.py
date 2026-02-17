import hashlib
p, s = "cat", "99" # Pass and Salt
combined = (s + p).encode() # Combine & bytes
h = hashlib.sha256(combined).hexdigest() # Hash it
print(f"Salted Hash: {h}") # Print result
