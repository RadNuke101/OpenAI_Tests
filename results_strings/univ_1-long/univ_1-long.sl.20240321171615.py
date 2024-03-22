# Prompt: return the first input, followed by a comma and space, and then the second input
# Given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA

def combine_inputs(input):
    return input[0] + ', ' + input[1]

# Test cases
print(combine_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # University of Pennsylvania, Phialdelphia, PA, USA
print(combine_inputs(['UCLA', 'Los Angeles, CA']))  # UCLA, Los Angeles, CA
print(combine_inputs(['Cornell University', 'Ithaca, New York, USA']))  # Cornell University, Ithaca, New York, USA
print(combine_inputs(['Penn', 'Philadelphia, PA, USA']))  # Penn, Philadelphia, PA, USA
print(combine_inputs(['University of Maryland College Park', 'College Park, MD']))  # University of Maryland College Park, College Park, MD
