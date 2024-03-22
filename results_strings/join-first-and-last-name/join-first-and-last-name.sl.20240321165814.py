# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_inputs(input):
    return input[0] + ' ' + input[1]

# Test the function with the given inputs
print(combine_inputs(['susan', 'chang']))  # Output: susan chang
print(combine_inputs(['aaron', 'kim']))    # Output: aaron kim
