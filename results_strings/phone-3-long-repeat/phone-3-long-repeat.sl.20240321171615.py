# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

def format_phone_number(input_str):
    parts = input_str.split('-')
    formatted_number = '(' + parts[0] + ') ' + parts[1] + '-' + parts[2]
    return formatted_number

# Test the function with the provided input
input_str = '938-242-504'
output_str = format_phone_number(input_str)
print(output_str)  # Output: (938) 242-504
