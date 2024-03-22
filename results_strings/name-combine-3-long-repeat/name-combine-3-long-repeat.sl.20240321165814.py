# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def first_letter_period(input):
    first_name = input[0]
    first_letter = first_name[0]
    return first_letter + '. ' + input[1]

# Test the function with the given input
print(first_letter_period(['Launa', 'Withers']))  # Output should be L. Withers
