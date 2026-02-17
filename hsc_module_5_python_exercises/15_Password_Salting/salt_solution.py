import hashlib
p, s = "cat", "99"
combined = s + p
final = hashlib.sha256(combined.encode()).hexdigest()
print(final)