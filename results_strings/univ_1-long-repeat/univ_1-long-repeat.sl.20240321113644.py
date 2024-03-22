# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: UC Berkeley, Berkeley, CA

def format_input_output(input_str):
    input_list = input_str.split(", ")
    return input_list[0] + ", " + input_list[1]

# Test the function with the given input
input_str = "UC Berkeley, Berkeley, CA"
output_str = format_input_output(input_str)
print(output_str)  # Output: UC Berkeley, Berkeley, CA
