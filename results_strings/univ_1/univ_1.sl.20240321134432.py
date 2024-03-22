# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test the function with the given input
input_data = ['University of Pennsylvania', 'Phialdelphia, PA, USA']
output_data = format_input_output(input_data)
print(output_data)  # Output: University of Pennsylvania, Phialdelphia, PA, USA
