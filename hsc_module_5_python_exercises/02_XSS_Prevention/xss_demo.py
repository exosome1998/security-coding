# Demo: .replace() cleans dangerous characters
code = "<script>"
safe = code.replace("<", "&lt;")
print(f"Safe: {safe}")