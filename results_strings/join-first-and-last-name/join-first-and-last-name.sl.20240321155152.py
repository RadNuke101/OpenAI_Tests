# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_inputs(input):
    return input[0] + ' ' + input[1]

# Test the function
input1 = ['susan', 'chang']
output1 = combine_inputs(input1)
print(output1)  # Output: susan chang

input2 = ['aaron', 'kim']
output2 = combine_inputs(input2)
print(output2)  # Output: aaron kim
