# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] -> Output: Nancy
# Input: ['Andrew Cencici'] -> Output: Andrew
# Input: ['Jan Kotas'] -> Output: Jan
# Input: ['Mariya Sergienko'] -> Output: Mariya

def get_first_word(input_phrase):
    return input_phrase.split()[0]

# Test cases
print(get_first_word('Nancy FreeHafer'))  # Output: Nancy
print(get_first_word('Andrew Cencici'))  # Output: Andrew
print(get_first_word('Jan Kotas'))  # Output: Jan
print(get_first_word('Mariya Sergienko'))  # Output: Mariya
