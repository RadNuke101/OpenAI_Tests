# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def return_second_input(input_str):
    inputs = input_str.split(', ')
    if "USA" not in inputs[1]:
        return inputs[1] + ', USA'
    else:
        return inputs[1] + ', ' + inputs[2]

# Test the function with the provided input
input_str = 'University of California, Santa Barbara, Santa Barbara, CA, USA'
output_str = return_second_input(input_str)
print(output_str)  # Output: Santa Barbara, CA, USA
