def format_phone_number(input_str):
    input_str = input_str[0]  # Extract the string from the list
    first_three_nums = input_str.split('-')[0][:3]  # Get the first three numbers before the first "-"
    input_str = input_str.replace('-', ' ', 1)  # Replace the first "-" with a space
    output_str = input_str.replace(first_three_nums, f'({first_three_nums})', 1)  # Add parentheses around the first three numbers
    return output_str

# Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
# Input: ['+106 769-858-438']
# Output: +106 (769) 858-438

# Test the function
print(format_phone_number(['+106 769-858-438']))
