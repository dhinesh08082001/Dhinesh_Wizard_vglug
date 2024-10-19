# Initialize an empty dictionary
user_inputs = {}

# Get three inputs from the user
for i in range(1, 4):
    key = input(f"Enter key {i}: ")
    value = input(f"Enter value for '{key}': ")
    user_inputs[key] = value

# Print the resulting dictionary
print("Your dictionary:", user_inputs)

