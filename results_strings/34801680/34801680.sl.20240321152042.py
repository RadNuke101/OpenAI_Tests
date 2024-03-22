# Prompt: return expression after the space after the "=" sign
# Input: ['Name= ABC Retailers']
# Output: ABC Retailers

def extract_expression(input_str):
    # Extract the expression after the "=" sign
    output = input_str.split('= ')[1]
    return output

# Test the function with the provided inputs
input1 = 'Name= ABC Retailers'
output1 = extract_expression(input1)
print(output1)  # Output: ABC Retailers

input2 = ' ame= XYZ Suppliers'
output2 = extract_expression(input2)
print(output2)  # Output: XYZ Suppliers
