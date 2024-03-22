def get_second_word(input_str):
    words = input_str.split()
    if len(words) >= 2:
        return words[1]
    else:
        return "Input phrase must have at least two words"

# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: FreeHafer

# Test cases
print(get_second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(get_second_word('Andrew Cencici'))  # Output: Cencici
print(get_second_word('Jan Kotas'))  # Output: Kotas
print(get_second_word('Mariya Sergienko'))  # Output: Sergienko
print(get_second_word('Launa Withers'))  # Output: Withers
