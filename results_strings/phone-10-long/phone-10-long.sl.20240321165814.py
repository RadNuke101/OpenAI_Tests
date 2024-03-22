def format_phone_number(input_str):
    input_str = input_str[0]  # Extracting the string from the list
    parts = input_str.split('-')  # Splitting the string by "-"
    first_three_nums = parts[0][:3]  # Extracting the first three numbers before the first "-"
    formatted_number = input_str.replace('-', ' ', 1)  # Replace the first "-" with a space
    formatted_number = formatted_number.replace(first_three_nums, f'({first_three_nums})', 1)  # Add parentheses around the first three numbers
    return formatted_number

# Input: '+106 769-858-438'
# Output: '+106 (769) 858-438'
# Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
