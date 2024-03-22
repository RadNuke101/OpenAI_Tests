# Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
# Input: '+106 769-858-438'
# Output: +106 (769) 858-438

def format_phone_number(input_str):
    parts = input_str.split('-')
    first_part = parts[0]
    first_three_numbers = '(' + first_part[:3] + ')'
    rest_of_number = ' '.join(parts[1:])
    return first_part.replace('-', ' ') + ' ' + first_three_numbers + ' ' + rest_of_number

# Test the function with the given input
input_str = '+106 769-858-438'
output_str = format_phone_number(input_str)
print(output_str)  # Output should be +106 (769) 858-438
