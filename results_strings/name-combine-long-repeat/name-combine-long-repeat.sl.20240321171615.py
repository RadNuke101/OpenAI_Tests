def combine_names(input_str):
    names = input_str.split(',')
    return names[0].strip() + ' ' + names[1].strip()

# Prompt: return first input followed by a space, and then the second input
# Given input as ['Nancy', 'FreeHafer'] output is Nancy FreeHafer

# Test cases
print(combine_names('Nancy, FreeHafer'))  # Output: Nancy FreeHafer
print(combine_names('Andrew, Cencici'))   # Output: Andrew Cencici
print(combine_names('Jan, Kotas'))        # Output: Jan Kotas
print(combine_names('Mariya, Sergienko')) # Output: Mariya Sergienko
print(combine_names('Launa, Withers'))    # Output: Launa Withers
Nancy FreeHafer
Andrew Cencici
Jan Kotas
Mariya Sergienko
Launa Withers
