# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def return_second_input(input_list):
    second_input = input_list[1]
    if "USA" not in second_input:
        return second_input + ", USA"
    return second_input

# Test the function with the provided input
input1 = ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
print(return_second_input(input1))  # Output: Santa Barbara, CA, USA
