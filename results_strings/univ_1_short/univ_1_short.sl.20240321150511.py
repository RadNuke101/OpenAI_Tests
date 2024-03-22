# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test cases
print(format_input_output(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output(['Cornell University', 'Ithaca, New York, USA']))  # Cornell University, Ithaca, New York, USA
print(format_input_output(['University of Maryland College Park', 'College Park, MD']))  # University of Maryland College Park, College Park, MD
print(format_input_output(['University of Michigan', 'Ann Arbor, MI, USA']))  # University of Michigan, Ann Arbor, MI, USA
print(format_input_output(['Yale University', 'New Haven, CT, USA']))  # Yale University, New Haven, CT, USA
print(format_input_output(['Columbia University', 'New York, NY, USA']))  # Columbia University, New York, NY, USA
