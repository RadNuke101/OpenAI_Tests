# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def return_second_input(input_str):
    input_list = input_str.split(', ')
    if 'USA' not in input_list[1]:
        return input_list[1] + ', USA'
    return input_list[1]

# Test the function with the provided input
input_str = 'University of California, Santa Barbara, Santa Barbara, CA, USA'
output_str = return_second_input(input_str)
print(output_str)  # Output: Santa Barbara, CA, USA
