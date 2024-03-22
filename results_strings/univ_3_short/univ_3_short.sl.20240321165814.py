# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def return_second_input(input):
    if "USA" not in input:
        return input + ", USA"
    return input

# Test cases
print(return_second_input('University of Pennsylvania'))
print(return_second_input('UCLA'))
print(return_second_input('Cornell University'))
print(return_second_input('Penn'))
print(return_second_input('University of Maryland College Park'))
print(return_second_input('University of Michigan'))
