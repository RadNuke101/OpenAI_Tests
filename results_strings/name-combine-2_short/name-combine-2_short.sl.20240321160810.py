# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def format_names(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    
    formatted_output = first_name + ' ' + last_name[0] + '.'
    
    return formatted_output

# Test cases
print(format_names(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(format_names(['Andrew', 'Cencici']))    # Output: Andrew C.
print(format_names(['Jan', 'Kotas']))         # Output: Jan K.
print(format_names(['Mariya', 'Sergienko']))  # Output: Mariya S.
Nancy F.
Andrew C.
Jan K.
Mariya S.
