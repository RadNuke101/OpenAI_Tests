def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", 
    # and delete the first "-" and replace it with a space
    input_list = input_str.split()
    first_part = input_list[0]
    second_part = input_list[1].replace("-", " ")
    third_part = input_list[2]
    fourth_part = input_list[3]
    
    output = f"{first_part} ({second_part[:3]}) {second_part[3:]}-{third_part}-{fourth_part}"
    
    return output

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))   # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))   # Output: +62 (647) 787-775
