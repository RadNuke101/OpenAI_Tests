def combine_inputs(inputs):
    # Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end
    return inputs[0][0] + inputs[1] + '_' + inputs[2]

# Test cases
print(combine_inputs(['ayako', 'ogawa', 'acme.com']))  # Output: aogawa_acme.com
print(combine_inputs(['amy', 'johnson', 'google.com']))  # Output: ajohnson_google.com
print(combine_inputs(['tom', 'chang', 'upenn.edu']))  # Output: tchang_upenn.edu
aogawa_acme.com
ajohnson_google.com
tchang_upenn.edu
