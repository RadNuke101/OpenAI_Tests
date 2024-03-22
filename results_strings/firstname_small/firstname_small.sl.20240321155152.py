# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: Nancy

def first_word(input):
    # Extract the first word from the input
    first_word = input[0].split()[0]
    return first_word

# Test cases
print(first_word(['Nancy FreeHafer']))  # Output: Nancy
print(first_word(['Andrew Cencici']))   # Output: Andrew
print(first_word(['Jan Kotas']))         # Output: Jan
print(first_word(['Mariya Sergienko']))  # Output: Mariya
