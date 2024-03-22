def get_first_word(input_str):
    return input_str.split()[0]

# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: Nancy
# Input: ['Andrew Cencici'] 
# Output: Andrew
# Input: ['Jan Kotas'] 
# Output: Jan
# Input: ['Mariya Sergienko'] 
# Output: Mariya
# Input: ['Launa Withers'] 
# Output: Launa
# Add more input/output examples as needed

# Test cases
print(get_first_word('Nancy FreeHafer'))  # Output: Nancy
print(get_first_word('Andrew Cencici'))  # Output: Andrew
print(get_first_word('Jan Kotas'))  # Output: Jan
print(get_first_word('Mariya Sergienko'))  # Output: Mariya
print(get_first_word('Launa Withers'))  # Output: Launa
