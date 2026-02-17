import os
request = "../private_data.txt" # Attack attempt
safe_name = os.path.basename(request) # Removes '../'
final_path = "images/" + safe_name # Forces into safe folder
print(f"Requested: {final_path}") # Safe path result
