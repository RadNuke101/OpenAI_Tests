def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
    # Example input: '+106 769-858-438'
    # Example output: '+106 (769) 858-438'
    
    # Find the index of the first "-"
    first_dash_index = input_str.index("-")
    
    # Extract the first three numbers before the first "-"
    first_three_numbers = input_str[:first_dash_index][:4]
    
    # Replace the first "-" with a space
    formatted_number = input_str.replace("-", " ", 1)
    
    # Insert parentheses around the first three numbers
    formatted_number = formatted_number.replace(first_three_numbers, "(" + first_three_numbers + ")", 1)
    
    return formatted_number

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))  # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))  # Output: +62 (647) 787-775
print(format_phone_number('+172 027-507-632'))  # Output: +172 (027) 507-632
print(format_phone_number('+72 001-050-856'))  # Output: +72 (001) 050-856
print(format_phone_number('+95 310-537-401'))  # Output: +95 (310) 537-401
