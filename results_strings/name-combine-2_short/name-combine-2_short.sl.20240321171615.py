# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def generate_output(input):
    first_name = input[0]
    last_name = input[1]
    
    output = first_name + ' ' + last_name[0] + '.'
    
    return output

# Test cases
print(generate_output(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(generate_output(['Andrew', 'Cencici']))    # Output: Andrew C.
print(generate_output(['Jan', 'Kotas']))         # Output: Jan K.
print(generate_output(['Mariya', 'Sergienko']))  # Output: Mariya S.
Nancy F.
Andrew C.
Jan K.
Mariya S.
