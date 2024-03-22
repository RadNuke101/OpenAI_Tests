# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def format_name(input):
    first_letter = input[0][0]
    result = first_letter + ". " + input[1]
    return result

# Test the function with the given input
input = ['Launa', 'Withers']
output = format_name(input)
print(output)  # Output should be L. Withers
