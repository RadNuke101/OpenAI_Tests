# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def format_names(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    
    formatted_name = first_name + ' ' + last_name[0] + '.'
    
    return formatted_name

# Test the function with the provided inputs
print(format_names(['Nancy', 'FreeHafer']))  # Output: Nancy F.
