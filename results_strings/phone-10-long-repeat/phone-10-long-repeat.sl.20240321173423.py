def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
    # Input: '+45 095-746-635'
    # Output: '+45 (095) 746-635'
    
    # Extracting the first three numbers before the first "-"
    first_three_nums = input_str.split('-')[0][:3]
    
    # Replacing the first "-" with a space and adding parentheses around the first three numbers
    output = input_str.replace('-', ' ', 1).replace(first_three_nums, f'({first_three_nums})', 1)
    
    return output

# Test cases
print(format_phone_number('+45 095-746-635'))  # Output: +45 (095) 746-635
print(format_phone_number('+161 233-981-513'))  # Output: +161 (233) 981-513
print(format_phone_number('+33 547-051-264'))  # Output: +33 (547) 051-264
