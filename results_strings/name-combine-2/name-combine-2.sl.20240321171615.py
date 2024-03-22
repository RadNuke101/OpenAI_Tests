# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer'] 
# Output: Nancy F.

def format_output(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    
    output = first_name + ' ' + last_name[0] + '.'
    
    return output

# Test cases
print(format_output(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(format_output(['Andrew', 'Cencici']))    # Output: Andrew C.
print(format_output(['Jan', 'Kotas']))          # Output: Jan K.
print(format_output(['Mariya', 'Sergienko']))   # Output: Mariya S.
Nancy F.
Andrew C.
Jan K.
Mariya S.
