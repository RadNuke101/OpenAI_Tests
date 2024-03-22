def format_names(input):
    return input[1] + ', ' + input[0][0] + '.'

# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.
print(format_names(['Launa', 'Withers']))

# Input: ['Lakenya', 'Edison']
# Output: Edison, L.
print(format_names(['Lakenya', 'Edison']))

# Input: ['Brendan', 'Hage']
# Output: Hage, B.
print(format_names(['Brendan', 'Hage']))

# Add more test cases if needed

