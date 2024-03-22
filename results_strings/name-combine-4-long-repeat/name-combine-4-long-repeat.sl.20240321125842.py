# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_name(input):
    return input[1] + ', ' + input[0][0] + '.'

# Test the function with the given input
input1 = ['Launa', 'Withers']
print(format_name(input1))  # Output: Withers, L.
