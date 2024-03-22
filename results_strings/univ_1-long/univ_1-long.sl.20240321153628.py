# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def combine_inputs(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test the function with the given inputs
print(combine_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(combine_inputs(['UCLA', 'Los Angeles, CA']))  # Output: UCLA, Los Angeles, CA
print(combine_inputs(['Cornell University', 'Ithaca, New York, USA']))  # Output: Cornell University, Ithaca, New York, USA
print(combine_inputs(['Penn', 'Philadelphia, PA, USA']))  # Output: Penn, Philadelphia, PA, USA
print(combine_inputs(['University of Maryland College Park', 'College Park, MD']))  # Output: University of Maryland College Park, College Park, MD
print(combine_inputs(['University of Michigan', 'Ann Arbor, MI, USA']))  # Output: University of Michigan, Ann Arbor, MI, USA
print(combine_inputs(['UC Berkeley', 'Berkeley, CA']))  # Output: UC Berkeley, Berkeley, CA
print(combine_inputs(['MIT', 'Cambridge, MA']))  # Output: MIT, Cambridge, MA
print(combine_inputs(['Rice University', 'Houston, TX']))  # Output: Rice University, Houston, TX
print(combine_inputs(['Yale University', 'New Haven, CT, USA']))  # Output: Yale University, New Haven, CT, USA
print(combine_inputs(['Columbia University', 'New York, NY, USA']))  # Output: Columbia University, New York, NY, USA
print(combine_inputs(['NYU', 'New York, New York, USA']))  # Output: NYU, New York, New York, USA
print(combine_inputs(['UC Berkeley', 'Berkeley, CA']))  # Output: UC Berkeley, Berkeley, CA
print(combine_inputs(['UIUC', 'Urbana, IL']))  # Output: UIUC, Urbana, IL
print(combine_inputs(['Temple University', 'Philadelphia, PA']))  # Output: Temple University, Philadelphia, PA
print(combine_inputs(['Harvard University', 'Cambridge, MA, USA']))  # Output: Harvard University, Cambridge, MA, USA
print(combine_inputs(['University of Connecticut', 'Storrs, CT, USA']))  # Output: University of Connecticut, Storrs, CT, USA
print(combine_inputs(['Drexel University', 'Philadelphia, PA']))  # Output: Drexel University, Philadelphia, PA
print(combine_inputs(['New Haven University', 'New Haven, CT, USA']))  # Output: New Haven University, New Haven, CT, USA
print(combine_inputs(['University of California, Santa Barbara', 'Santa Barbara, CA, USA']))  # Output: University of California, Santa Barbara, Santa Barbara, CA, USA
