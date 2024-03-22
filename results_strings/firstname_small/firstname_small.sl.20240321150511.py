# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: Nancy

def get_first_word(input_phrase):
    # Extract the first word from the input phrase
    first_word = input_phrase[0].split()[0]
    return first_word

# Test cases
print(get_first_word(['Nancy FreeHafer']))  # Output: Nancy
print(get_first_word(['Andrew Cencici']))   # Output: Andrew
print(get_first_word(['Jan Kotas']))         # Output: Jan
print(get_first_word(['Mariya Sergienko']))  # Output: Mariya
