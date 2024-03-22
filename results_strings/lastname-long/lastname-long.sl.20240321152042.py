def get_second_word(input_phrase):
    words = input_phrase.split()
    return words[1]

# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer']
# Output: FreeHafer

# Test cases
print(get_second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(get_second_word('Andrew Cencici'))   # Output: Cencici
print(get_second_word('Jan Kotas'))        # Output: Kotas
print(get_second_word('Mariya Sergienko')) # Output: Sergienko
print(get_second_word('Launa Withers'))    # Output: Withers
