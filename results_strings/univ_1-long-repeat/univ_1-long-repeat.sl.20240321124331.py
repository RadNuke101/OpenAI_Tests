# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: University of California, Santa Barbara, Santa Barbara, CA, USA

def combine_inputs(input):
    return input[0] + ', ' + input[1]

# Test the function with the given input
input = ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
output = combine_inputs(input)
print(output)  # University of California, Santa Barbara, Santa Barbara, CA, USA
