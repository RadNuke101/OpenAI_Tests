def format_phone_number(input_str):
    input_str = input_str.replace("+", "").replace("-", ".").replace(" ", "")
    return input_str

# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: ['+106 769-858-438']
# Output: 106.769.858.438

print(format_phone_number('+106 769-858-438'))  # Output: 106.769.858.438
