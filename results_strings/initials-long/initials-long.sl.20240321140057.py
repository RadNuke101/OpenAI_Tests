def get_initials(input_str):
    words = input_str.split()
    initials = words[0][0].upper() + '.' + words[1][0].upper() + '.'
    return initials

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.

print(get_initials('Nancy FreeHafer'))  # N.F.
print(get_initials('Andrew Cencici'))  # A.C.
print(get_initials('Jan Kotas'))  # J.K.
print(get_initials('Mariya Sergienko'))  # M.S.
print(get_initials('Launa Withers'))  # L.W.
print(get_initials('Lakenya Edison'))  # L.E.
# Add more test cases if needed
