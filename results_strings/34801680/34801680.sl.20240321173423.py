# Prompt: return expression after the space after the "=" sign
# Input: 'Name= ABC Retailers'
# Output: 'ABC Retailers'

def extract_expression(input_string):
    return input_string.split('= ')[1]

# Test cases
input1 = 'Name= ABC Retailers'
output1 = extract_expression(input1)
print(output1)  # Output: 'ABC Retailers'

input2 = ' ame= XYZ Suppliers'
output2 = extract_expression(input2)
print(output2)  # Output: 'XYZ Suppliers'
