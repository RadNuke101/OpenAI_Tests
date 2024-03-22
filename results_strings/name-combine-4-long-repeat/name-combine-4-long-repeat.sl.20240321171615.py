# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_name(input):
    return input[1] + ', ' + input[0][0] + '.'

# Test the function with the provided input
print(format_name(['Launa', 'Withers']))  # Output should be Withers, L.
