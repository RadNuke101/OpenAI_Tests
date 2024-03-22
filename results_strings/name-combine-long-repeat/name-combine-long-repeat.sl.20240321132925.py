def combine_names(input_str):
    names = input_str.split()
    return names[0] + " " + names[1]

# Prompt: return first input followed by a space, and then the second input
# Input: ['Nancy', 'FreeHafer'] Output: Nancy FreeHafer
# Input: ['Andrew', 'Cencici'] Output: Andrew Cencici
# Input: ['Jan', 'Kotas'] Output: Jan Kotas

# Test the function with the provided inputs
print(combine_names('Nancy FreeHafer'))  # Output: Nancy FreeHafer
print(combine_names('Andrew Cencici'))  # Output: Andrew Cencici
print(combine_names('Jan Kotas'))  # Output: Jan Kotas
Nancy FreeHafer
Andrew Cencici
Jan Kotas
