# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: ['+106 769-858-438']
# Output: '106.769.858.438'

def format_phone_number(input):
    input = input[0].replace("+", "").replace(" ", ".").replace("-", ".")
    return input

# Test cases
print(format_phone_number(['+106 769-858-438'])) # Output: '106.769.858.438'
print(format_phone_number(['+83 973-757-831'])) # Output: '83.973.757.831'
print(format_phone_number(['+62 647-787-775'])) # Output: '62.647.787.775'
