# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: '+106 769-858-438'
# Output: '106.769.858.438'

def format_phone_number(input_str):
    output = input_str.replace("+", "").replace(" ", ".").replace("-", ".")
    return output

# Test the function with the provided inputs
print(format_phone_number('+106 769-858-438'))  # Output should be '106.769.858.438'
print(format_phone_number('+83 973-757-831'))  # Output should be '83.973.757.831'
print(format_phone_number('+62 647-787-775'))  # Output should be '62.647.787.775'
print(format_phone_number('+172 027-507-632'))  # Output should be '172.027.507.632'
print(format_phone_number('+72 001-050-856'))  # Output should be '72.001.050.856'
print(format_phone_number('+95 310-537-401'))  # Output should be '95.310.537.401'
