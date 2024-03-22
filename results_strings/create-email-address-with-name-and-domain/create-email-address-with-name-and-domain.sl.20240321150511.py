# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end

def generate_output(inputs):
    first_letter = inputs[0][0]
    second_input = inputs[1]
    third_input = inputs[2]
    
    output = first_letter + second_input + "_" + third_input
    return output

# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com

# Input: ['amy', 'johnson', 'google.com']
# Output: ajohnson_google.com

# Input: ['tom', 'chang', 'upenn.edu']
# Output: tchang_upenn.edu
