# Prompt: return expression after the space after the "=" sign
# Input: 'Name= ABC Retailers'
# Output: 'ABC Retailers'

def extract_expression(input_str):
    return input_str.split('= ')[1]

# Test cases
print(extract_expression('Name= ABC Retailers'))  # Output: 'ABC Retailers'
print(extract_expression(' ame= XYZ Suppliers'))  # Output: 'XYZ Suppliers'
