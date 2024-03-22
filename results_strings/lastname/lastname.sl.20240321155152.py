# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] -> Output: FreeHafer
# Input: ['Andrew Cencici'] -> Output: Cencici
# Input: ['Jan Kotas'] -> Output: Kotas
# Input: ['Mariya Sergienko'] -> Output: Sergienko

def get_second_word(input_phrase):
    words = input_phrase.split()
    if len(words) >= 2:
        return words[1]
    else:
        return "Input phrase does not contain a second word."

# Test cases
print(get_second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(get_second_word('Andrew Cencici'))    # Output: Cencici
print(get_second_word('Jan Kotas'))         # Output: Kotas
print(get_second_word('Mariya Sergienko'))  # Output: Sergienko
FreeHafer
Cencici
Kotas
Sergienko
