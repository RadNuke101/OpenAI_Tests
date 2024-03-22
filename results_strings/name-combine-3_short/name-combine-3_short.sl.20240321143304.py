def format_names(input):
    first_letter = input[0][0]
    formatted_output = first_letter + '. ' + input[1]
    return formatted_output

# Input: ['Launa', 'Withers']
# Output: L. Withers
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input

print(format_names(['Launa', 'Withers']))  # Output: L. Withers
print(format_names(['Lakenya', 'Edison']))  # Output: L. Edison
print(format_names(['Brendan', 'Hage']))  # Output: B. Hage
print(format_names(['Bradford', 'Lango']))  # Output: B. Lango
print(format_names(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(format_names(['Lara', 'Constable']))  # Output: L. Constable
