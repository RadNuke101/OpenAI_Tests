# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: Nancy

def first_word(input_phrase):
    return input_phrase.split()[0]

# Test cases
print(first_word('Nancy FreeHafer'))  # Output: Nancy
print(first_word('Andrew Cencici'))    # Output: Andrew
print(first_word('Jan Kotas'))         # Output: Jan
print(first_word('Mariya Sergienko'))  # Output: Mariya
