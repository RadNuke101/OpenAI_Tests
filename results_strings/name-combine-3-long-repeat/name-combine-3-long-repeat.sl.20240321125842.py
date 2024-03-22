# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def first_letter_period(input):
    first_name = input[0][0]
    result = first_name + ". " + input[1]
    return result

# Test the function with the given input
input = ['Launa', 'Withers']
output = first_letter_period(input)
print(output)  # Output should be L. Withers
