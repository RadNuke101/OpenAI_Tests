# Prompt: return expression after the space after the "=" sign
# Input: 'Name= ABC Retailers'
# Output: 'ABC Retailers'

def get_expression_after_equal_sign(input_string):
    return input_string.split('= ')[1]

# Test cases
print(get_expression_after_equal_sign('Name= ABC Retailers'))  # Output: 'ABC Retailers'
print(get_expression_after_equal_sign(' ame= XYZ Suppliers'))  # Output: 'XYZ Suppliers'
