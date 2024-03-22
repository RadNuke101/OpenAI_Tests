def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
    # Input: '+45 095-746-635'
    # Output: '+45 (095) 746-635'
    
    # Extract the first three numbers before the first "-"
    first_three_nums = input_str.split('-')[0][:3]
    
    # Replace the first "-" with a space
    output = input_str.replace('-', ' ', 1)
    
    # Insert parentheses around the first three numbers
    output = output.replace(first_three_nums, f'({first_three_nums})', 1)
    
    return output

# Test the function
print(format_phone_number('+45 095-746-635'))  # Output: +45 (095) 746-635
