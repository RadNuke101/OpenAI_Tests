# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def format_output(inputs):
    first_letter = inputs[0][0]
    output = first_letter + ". " + inputs[1]
    return output

# Test the function with the given inputs
input1 = ['Launa', 'Withers']
print(format_output(input1))  # Output: L. Withers

input2 = ['Lakenya', 'Edison']
print(format_output(input2))  # Output: L. Edison
