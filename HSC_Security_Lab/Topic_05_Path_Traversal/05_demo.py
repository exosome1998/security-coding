import os # OS library
path = "../../etc/config" # Dangerous path
print(f"Safe: {os.path.basename(path)}") # Returns just 'config'
