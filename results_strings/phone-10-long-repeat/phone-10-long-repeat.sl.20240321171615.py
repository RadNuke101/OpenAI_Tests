# Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
# Input: '+106 769-858-438'
# Output: +106 (769) 858-438

def format_phone_number(input_str):
    parts = input_str.split('-')
    first_three = '(' + parts[0][-3:] + ')'
    new_input = parts[0][:-3] + first_three + ' ' + '-'.join(parts[1:])
    return new_input

# Test the function with the given input
input_str = '+106 769-858-438'
output_str = format_phone_number(input_str)
print(output_str)  # Output should be +106 (769) 858-438
