# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_names(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    
    output = last_name + ', ' + first_name[0] + '.'
    
    return output

# Test the function with the provided input
input_data = ['Launa', 'Withers']
print(format_names(input_data))  # Output: Withers, L.
