# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input):
    return input[0] + ', ' + input[1]

# Test the function with the given inputs
print(format_input_output(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_input_output(['Cornell University', 'Ithaca, New York, USA']))
print(format_input_output(['University of Maryland College Park', 'College Park, MD']))
print(format_input_output(['University of Michigan', 'Ann Arbor, MI, USA']))
print(format_input_output(['Yale University', 'New Haven, CT, USA']))
print(format_input_output(['Columbia University', 'New York, NY, USA']))
University of Pennsylvania, Phialdelphia, PA, USA
Cornell University, Ithaca, New York, USA
University of Maryland College Park, College Park, MD
University of Michigan, Ann Arbor, MI, USA
Yale University, New Haven, CT, USA
Columbia University, New York, NY, USA
