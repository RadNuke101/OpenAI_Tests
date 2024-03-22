# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] -> Output: Nancy
# Input: ['Andrew Cencici'] -> Output: Andrew
# Input: ['Jan Kotas'] -> Output: Jan

def first_word(input_str):
    return input_str.split()[0]

# Test cases
print(first_word('Nancy FreeHafer')) # Output: Nancy
print(first_word('Andrew Cencici')) # Output: Andrew
print(first_word('Jan Kotas')) # Output: Jan
