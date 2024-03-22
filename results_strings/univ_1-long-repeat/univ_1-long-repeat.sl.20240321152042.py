# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: UC Berkeley, Berkeley, CA

def combine_inputs(input):
    return input[0] + ', ' + input[1]

# Test the function with the given input
input = ['UC Berkeley', 'Berkeley, CA']
output = combine_inputs(input)
print(output)  # UC Berkeley, Berkeley, CA
