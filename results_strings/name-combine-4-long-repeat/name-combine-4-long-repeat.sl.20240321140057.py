def format_names(input):
    first_name = input[0]
    last_name = input[1]
    output = last_name + ', ' + first_name[0] + '.'
    return output

# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))  # Output: Hage, B.
