import hashlib
user_pwd = "AdminPassword"
h_obj = hashlib.sha256(user_pwd.encode())
final = h_obj.hexdigest()
print(f"Secure Hash: {final}")