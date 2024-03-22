# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test cases
print(format_input_output(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output(['UCLA', 'Los Angeles, CA']))  # UCLA, Los Angeles, CA
print(format_input_output(['Cornell University', 'Ithaca, New York, USA']))  # Cornell University, Ithaca, New York, USA
