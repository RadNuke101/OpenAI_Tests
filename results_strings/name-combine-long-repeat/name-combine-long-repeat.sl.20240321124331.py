# Prompt: return first input followed by a space, and then the second input
# Input: ['Nancy', 'FreeHafer'] 
# Output: Nancy FreeHafer

def combine_names(input):
    return input[0] + ' ' + input[1]

# Test the function with the provided inputs
print(combine_names(['Nancy', 'FreeHafer']))  # Output: Nancy FreeHafer
print(combine_names(['Andrew', 'Cencici']))   # Output: Andrew Cencici
print(combine_names(['Jan', 'Kotas']))        # Output: Jan Kotas
