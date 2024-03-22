def format_names(input):
    # Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
    return input[1] + ', ' + input[0][0] + '.'

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_names(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_names(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
print(format_names(['Lara', 'Constable']))  # Output: Constable, L.
print(format_names(['Madelaine', 'Ghoston']))  # Output: Ghoston, M.
# Add more test cases if needed
