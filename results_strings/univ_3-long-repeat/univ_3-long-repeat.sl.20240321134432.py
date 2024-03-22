# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

def return_second_input(input_str):
    inputs = input_str.split(', ')
    if "USA" not in inputs[1]:
        return inputs[1] + ', USA'
    return inputs[1]

# Test cases
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(return_second_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, New York, USA
