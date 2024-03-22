# Prompt: return expression after the space after the "=" sign
# Input: 'Name= ABC Retailers'
# Output: 'ABC Retailers'

def get_expression_after_equal_sign(input_string):
    # Split the input string by the "=" sign
    split_input = input_string.split('=')
    
    # Get the expression after the "=" sign
    output = split_input[1].strip()
    
    return output

# Test cases
input1 = 'Name= ABC Retailers'
input2 = ' ame= XYZ Suppliers'

print(get_expression_after_equal_sign(input1))  # Output: 'ABC Retailers'
print(get_expression_after_equal_sign(input2))  # Output: 'XYZ Suppliers'
