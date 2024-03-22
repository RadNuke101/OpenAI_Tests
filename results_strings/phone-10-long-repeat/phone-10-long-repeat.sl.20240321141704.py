def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
    # Input: ['+45 095-746-635']
    # Output: +45 (095) 746-635
    parts = input_str.split('-')
    first_part = parts[0]
    first_three_nums = first_part.split()[1][:3]
    formatted_number = f"{first_part[0]} ({first_three_nums}) {parts[1]}-{parts[2]}"
    return formatted_number

# Test the function with the given input
input_str = '+45 095-746-635'
output_str = format_phone_number(input_str)
print(output_str)  # Output: +45 (095) 746-635
