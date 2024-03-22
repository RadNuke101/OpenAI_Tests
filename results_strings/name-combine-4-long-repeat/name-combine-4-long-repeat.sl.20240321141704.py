def format_names(input):
    # Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
    return input[1] + ', ' + input[0][0] + '.'

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_names(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_names(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
Withers, L.
Edison, L.
Hage, B.
Lango, B.
Akiyama, R.
