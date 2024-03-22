# Prompt: return expression after the space after the "=" sign
# Input: ['Name= ABC Retailers']
# Output: ABC Retailers

def get_expression_after_equal_sign(input_str):
    return input_str.split('= ')[1]

# Test cases
input1 = 'Name= ABC Retailers'
output1 = get_expression_after_equal_sign(input1)
print(output1)  # Output: ABC Retailers

input2 = ' ame= XYZ Suppliers'
output2 = get_expression_after_equal_sign(input2)
print(output2)  # Output: XYZ Suppliers
