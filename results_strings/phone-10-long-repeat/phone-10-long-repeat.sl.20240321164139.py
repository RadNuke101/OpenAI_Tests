# Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
# Input: '+106 769-858-438'
# Output: +106 (769) 858-438

def format_phone_number(input_str):
    parts = input_str.split('-')
    first_part = parts[0]
    numbers = ''.join(filter(str.isdigit, first_part))
    formatted_number = '(' + numbers[:3] + ') ' + numbers[3:]
    return input_str.replace('-', ' ', 1).replace(numbers, formatted_number, 1)

# Test the function with the provided input
input_str = '+106 769-858-438'
output_str = format_phone_number(input_str)
print(output_str)  # Output should be +106 (769) 858-438
