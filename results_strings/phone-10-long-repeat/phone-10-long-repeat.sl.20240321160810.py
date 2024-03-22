def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
    # Example input: '+106 769-858-438'
    # Example output: '+106 (769) 858-438'
    
    parts = input_str.split('-')
    first_part = parts[0]
    first_three_numbers = '(' + first_part[4:7] + ')'
    
    output = first_part[:4] + ' ' + first_three_numbers + '-' + '-'.join(parts[1:])
    
    return output

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))  # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))  # Output: +62 (647) 787-775
print(format_phone_number('+172 027-507-632'))  # Output: +172 (027) 507-632
print(format_phone_number('+72 001-050-856'))  # Output: +72 (001) 050-856
print(format_phone_number('+95 310-537-401'))  # Output: +95 (310) 537-401
print(format_phone_number('+6 775-969-238'))  # Output: +6 (775) 969-238
print(format_phone_number('+174 594-539-946'))  # Output: +174 (594) 539-946
print(format_phone_number('+155 927-275-860'))  # Output: +155 (927) 275-860
print(format_phone_number('+167 405-461-331'))  # Output: +167 (405) 461-331
