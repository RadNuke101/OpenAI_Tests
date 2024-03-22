# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end
# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com

def generate_output(input_list):
    first_letter = input_list[0][0]
    second_input = input_list[1]
    third_input = input_list[2]
    
    output = first_letter + second_input + "_" + third_input
    return output

# Test cases
print(generate_output(['ayako', 'ogawa', 'acme.com']))  # Output: aogawa_acme.com
print(generate_output(['amy', 'johnson', 'google.com']))  # Output: ajohnson_google.com
print(generate_output(['tom', 'chang', 'upenn.edu']))  # Output: tchang_upenn.edu
aogawa_acme.com
ajohnson_google.com
tchang_upenn.edu
