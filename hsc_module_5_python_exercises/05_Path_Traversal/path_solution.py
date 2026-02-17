import os
request = "../private.txt"
safe = os.path.basename(request)
full_path = "images/" + safe
print(full_path)