# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer']
# Output: Nancy

def get_first_word(input_phrase):
    # Convert the input list to a string
    input_str = input_phrase[0]
    
    # Split the string by space and return the first word
    return input_str.split()[0]

# Test cases
print(get_first_word(['Nancy FreeHafer']))  # Output: Nancy
print(get_first_word(['Andrew Cencici']))   # Output: Andrew
print(get_first_word(['Jan Kotas']))         # Output: Jan
print(get_first_word(['Mariya Sergienko']))  # Output: Mariya
Nancy
Andrew
Jan
Mariya
