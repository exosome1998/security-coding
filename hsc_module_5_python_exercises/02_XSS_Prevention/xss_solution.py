comment = "Hello <script>alert(1)</script>"
clean = comment.replace("<", "").replace(">", "")
print(f"Sanitized: {clean}")