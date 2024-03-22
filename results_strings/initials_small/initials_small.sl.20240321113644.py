# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] Output: N.F.
# Input: ['Andrew Cencici'] Output: A.C.
# Input: ['Jan Kotas'] Output: J.K.
# Input: ['Mariya Sergienko'] Output: M.S.

def generate_output(input_str):
    words = input_str.split()
    output = words[0][0] + '.' + words[1][0] + '.'
    return output

# Test cases
print(generate_output('Nancy FreeHafer'))  # Output: N.F.
print(generate_output('Andrew Cencici'))   # Output: A.C.
print(generate_output('Jan Kotas'))        # Output: J.K.
print(generate_output('Mariya Sergienko')) # Output: M.S.
N.F.
A.C.
J.K.
M.S.
