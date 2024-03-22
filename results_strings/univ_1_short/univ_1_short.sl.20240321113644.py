# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def combine_inputs(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test cases
print(combine_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # University of Pennsylvania, Phialdelphia, PA, USA
print(combine_inputs(['Cornell University', 'Ithaca, New York, USA']))  # Cornell University, Ithaca, New York, USA
print(combine_inputs(['University of Maryland College Park', 'College Park, MD']))  # University of Maryland College Park, College Park, MD
print(combine_inputs(['University of Michigan', 'Ann Arbor, MI, USA']))  # University of Michigan, Ann Arbor, MI, USA
print(combine_inputs(['Yale University', 'New Haven, CT, USA']))  # Yale University, New Haven, CT, USA
print(combine_inputs(['Columbia University', 'New York, NY, USA']))  # Columbia University, New York, NY, USA
