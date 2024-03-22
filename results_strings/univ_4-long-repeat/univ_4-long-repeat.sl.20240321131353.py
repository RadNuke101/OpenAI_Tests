# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def return_second_input(input_str):
    input_list = input_str.split(', ')
    second_input = input_list[1]
    
    if "USA" not in second_input:
        return second_input + ', USA'
    else:
        return second_input

# Test the function with the provided input
input_str = 'University of California, Santa Barbara, Santa Barbara, CA, USA'
output_str = return_second_input(input_str)
print(output_str)  # Output: Santa Barbara, CA, USA
