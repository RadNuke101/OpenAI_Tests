def first_letters(input_str):
    words = input_str.split()
    output = words[0][0].upper() + '.' + words[1][0].upper() + '.'
    return output

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.
# Input: ['Andrew Cencici']
# Output: A.C.
# Input: ['Jan Kotas']
# Output: J.K.
# Input: ['Mariya Sergienko']
# Output: M.S.

# Test cases
print(first_letters('Nancy FreeHafer'))  # Output: N.F.
print(first_letters('Andrew Cencici'))    # Output: A.C.
print(first_letters('Jan Kotas'))         # Output: J.K.
print(first_letters('Mariya Sergienko'))  # Output: M.S.
