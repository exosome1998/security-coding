import secrets # Secure random lib
print(f"Token: {secrets.token_hex(4)}") # 8 hex chars
