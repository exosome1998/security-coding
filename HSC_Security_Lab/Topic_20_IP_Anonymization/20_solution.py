ip = "192.168.1.55" # User IP
p = ip.split(".") # Split into list
masked = f"{p[0]}.{p[1]}.{p[2]}.0" # Hide last part
print(f"Anon IP: {masked}") # Print result
