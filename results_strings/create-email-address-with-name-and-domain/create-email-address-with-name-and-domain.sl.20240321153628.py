# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end

def combine_inputs(input):
    first_letter = input[0][0]
    second_input = input[1]
    third_input = input[2]
    
    output = first_letter + second_input + "_" + third_input
    return output

# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com
print(combine_inputs(['ayako', 'ogawa', 'acme.com']))

# Input: ['amy', 'johnson', 'google.com']
# Output: ajohnson_google.com
print(combine_inputs(['amy', 'johnson', 'google.com']))

# Input: ['tom', 'chang', 'upenn.edu']
# Output: tchang_upenn.edu
print(combine_inputs(['tom', 'chang', 'upenn.edu']))
