def get_initials(input_str):
    words = input_str.split()
    initials = [word[0].upper() for word in words]
    return '.'.join(initials) + '.'

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.

# Test cases
print(get_initials('Nancy FreeHafer'))  # Output: N.F.
print(get_initials('Andrew Cencici'))  # Output: A.C.
print(get_initials('Jan Kotas'))  # Output: J.K.
print(get_initials('Mariya Sergienko'))  # Output: M.S.
print(get_initials('Launa Withers'))  # Output: L.W.
print(get_initials('Lakenya Edison'))  # Output: L.E.
