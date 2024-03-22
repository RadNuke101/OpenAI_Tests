# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: FreeHafer

def second_word(input_phrase):
    words = input_phrase.split()
    if len(words) >= 2:
        return words[1]
    else:
        return "No second word found"

# Test cases
print(second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(second_word('Andrew Cencici'))   # Output: Cencici
print(second_word('Jan Kotas'))         # Output: Kotas
print(second_word('Mariya Sergienko'))  # Output: Sergienko
