# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] Output: N.F.
# Input: ['Andrew Cencici'] Output: A.C.
# Input: ['Jan Kotas'] Output: J.K.
# Input: ['Mariya Sergienko'] Output: M.S.

def first_letters(input_phrase):
    words = input_phrase.split()
    first_letters = [word[0] for word in words]
    return '.'.join(first_letters) + '.'

# Test cases
print(first_letters('Nancy FreeHafer'))  # Output: N.F.
print(first_letters('Andrew Cencici'))    # Output: A.C.
print(first_letters('Jan Kotas'))         # Output: J.K.
print(first_letters('Mariya Sergienko'))  # Output: M.S.
N.F.
A.C.
J.K.
M.S.
