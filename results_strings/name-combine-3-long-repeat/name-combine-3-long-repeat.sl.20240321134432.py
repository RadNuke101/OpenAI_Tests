# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def first_letter_period(input):
    return input[0][0] + ". " + input[1]

# Test the function with the provided input
print(first_letter_period(['Launa', 'Withers']))  # Output: L. Withers
