# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] Output: N.F.
# Input: ['Andrew Cencici'] Output: A.C.
# Input: ['Jan Kotas'] Output: J.K.
# Input: ['Mariya Sergienko'] Output: M.S.

def get_initials(input_phrase):
    words = input_phrase[0].split()
    initials = words[0][0] + '.' + words[1][0] + '.'
    return initials

# Test cases
print(get_initials(['Nancy FreeHafer']))  # Output: N.F.
print(get_initials(['Andrew Cencici']))    # Output: A.C.
print(get_initials(['Jan Kotas']))         # Output: J.K.
print(get_initials(['Mariya Sergienko']))  # Output: M.S.
