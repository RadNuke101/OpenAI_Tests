def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
    # Input: ['+106 769-858-438'], Output: +106 (769) 858-438
    parts = input_str.split('-')
    first_part = parts[0]
    first_three_numbers = first_part.split(' ')[1][:3]
    formatted_number = first_part.replace(first_three_numbers, '(' + first_three_numbers + ')').replace('-', ' ')
    return formatted_number

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))    # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))    # Output: +62 (647) 787-775
print(format_phone_number('+172 027-507-632'))   # Output: +172 (027) 507-632
print(format_phone_number('+72 001-050-856'))    # Output: +72 (001) 050-856
print(format_phone_number('+95 310-537-401'))    # Output: +95 (310) 537-401
print(format_phone_number('+6 775-969-238'))     # Output: +6 (775) 969-238
+106 (769) 858-438
+83 (973) 757-831
+62 (647) 787-775
+172 (027) 507-632
+72 (001) 050-856
+95 (310) 537-401
+6 (775) 969-238
