comment = "Hello <script>alert(1)</script>" # Dangerous input
clean = comment.replace("<", "").replace(">", "") # Remove both brackets
print(f"Sanitized: {clean}") # Output is safe text
