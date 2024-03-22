# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: FreeHafer

def second_word(input_phrase):
    words = input_phrase.split()
    return words[1]

# Test cases
print(second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(second_word('Andrew Cencici'))    # Output: Cencici
print(second_word('Jan Kotas'))         # Output: Kotas
print(second_word('Mariya Sergienko'))  # Output: Sergienko
