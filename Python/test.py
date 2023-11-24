import re

# Regular expression pattern
pattern = r"^(0(\.\d{1,2})?|1(\.0{1,2})?|[0-9](\.\d{1,2})?)$"

# Input from the user
user_input = input("Enter a value between 0.0 and 1.0: ")

# Validate the user input
if re.match(pattern, user_input):
    value = float(user_input)
    if value > 1.0:
        print("Value should be 1.0 or less. Setting value to 1.0.")
        value = 1.0
    print(f"Valid value: {value}")
else:
    print("Invalid input. Please enter a value between 0.0 and 1.0.")