# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: UC Berkeley, Berkeley, CA

def combine_inputs(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test the function with the given input
input_data = ['UC Berkeley', 'Berkeley, CA']
output_data = combine_inputs(input_data)
print(output_data)  # Output should be: UC Berkeley, Berkeley, CA
