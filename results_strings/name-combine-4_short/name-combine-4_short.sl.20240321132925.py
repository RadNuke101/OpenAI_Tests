# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_name(input):
    return input[1] + ', ' + input[0][0] + '.'

# Test cases
print(format_name(['Launa', 'Withers']))  # Output: Withers, L.
print(format_name(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_name(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_name(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_name(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
Withers, L.
Edison, L.
Hage, B.
Lango, B.
Akiyama, R.
