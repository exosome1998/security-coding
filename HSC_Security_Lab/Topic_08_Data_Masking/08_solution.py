my_id = "ID-9988-77" # Sensitive data
hidden = my_id[0:3] + "****" + my_id[-2:] # Slice & mask
print(f"Masked ID: {hidden}") # Show safe version
