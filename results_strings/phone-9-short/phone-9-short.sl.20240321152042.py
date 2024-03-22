# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: '+106 769-858-438'
# Output: '106.769.858.438'

def format_phone_number(phone_number):
    phone_number = phone_number.replace('+', '').replace(' ', '.').replace('-', '.')
    return phone_number

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: '106.769.858.438'
print(format_phone_number('+83 973-757-831'))    # Output: '83.973.757.831'
print(format_phone_number('+62 647-787-775'))    # Output: '62.647.787.775'
print(format_phone_number('+172 027-507-632'))   # Output: '172.027.507.632'
print(format_phone_number('+72 001-050-856'))    # Output: '72.001.050.856'
print(format_phone_number('+95 310-537-401'))    # Output: '95.310.537.401'
print(format_phone_number('+6 775-969-238'))     # Output: '6.775.969.238'
