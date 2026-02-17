user_role = "hacker" # Invalid role
valid_roles = ["student", "teacher"] # Allowed list
is_ok = user_role in valid_roles # strict check
if not is_ok: # If false
    print("Blocked") # Block access
