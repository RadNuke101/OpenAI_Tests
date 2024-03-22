# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: Nancy

def first_word(input):
    # Convert the input list to a string
    input_str = input[0]
    
    # Split the input string by space and return the first word
    return input_str.split()[0]

# Test cases
print(first_word(['Nancy FreeHafer']))  # Output: Nancy
print(first_word(['Andrew Cencici']))    # Output: Andrew
print(first_word(['Jan Kotas']))          # Output: Jan
print(first_word(['Mariya Sergienko']))   # Output: Mariya
Nancy
Andrew
Jan
Mariya
