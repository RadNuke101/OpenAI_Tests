# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_name(input):
    first_name = input[0]
    last_name = input[1]
    formatted_name = last_name + ', ' + first_name[0] + '.'
    return formatted_name

# Test the function with the provided inputs
print(format_name(['Launa', 'Withers']))  # Output: Withers, L.
print(format_name(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_name(['Brendan', 'Hage']))  # Output: Hage, B.
