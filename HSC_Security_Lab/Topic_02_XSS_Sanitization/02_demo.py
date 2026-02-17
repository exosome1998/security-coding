code = "<script>" # Dangerous HTML tag
safe = code.replace("<", "&lt;") # Swap '<' with safe HTML entity
print(f"Safe: {safe}") # Browser sees text, not code
