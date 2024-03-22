# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] Output: N.F.
# Input: ['Andrew Cencici'] Output: A.C.
# Input: ['Jan Kotas'] Output: J.K.
# Input: ['Mariya Sergienko'] Output: M.S.

def first_letters(input_phrase):
    words = input_phrase[0].split()
    output = words[0][0] + '.' + words[1][0] + '.'
    return output

# Test cases
print(first_letters(['Nancy FreeHafer']))  # Output: N.F.
print(first_letters(['Andrew Cencici']))    # Output: A.C.
print(first_letters(['Jan Kotas']))          # Output: J.K.
print(first_letters(['Mariya Sergienko']))   # Output: M.S.
