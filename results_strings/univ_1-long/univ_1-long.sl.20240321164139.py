# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test cases
print(format_input_output(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output(['UCLA', 'Los Angeles, CA']))  # UCLA, Los Angeles, CA
print(format_input_output(['Cornell University', 'Ithaca, New York, USA']))  # Cornell University, Ithaca, New York, USA
print(format_input_output(['Penn', 'Philadelphia, PA, USA']))  # Penn, Philadelphia, PA, USA
print(format_input_output(['University of Maryland College Park', 'College Park, MD']))  # University of Maryland College Park, College Park, MD
print(format_input_output(['University of Michigan', 'Ann Arbor, MI, USA']))  # University of Michigan, Ann Arbor, MI, USA
print(format_input_output(['UC Berkeley', 'Berkeley, CA']))  # UC Berkeley, Berkeley, CA
print(format_input_output(['MIT', 'Cambridge, MA']))  # MIT, Cambridge, MA
print(format_input_output(['Rice University', 'Houston, TX']))  # Rice University, Houston, TX
print(format_input_output(['Yale University', 'New Haven, CT, USA']))  # Yale University, New Haven, CT, USA
print(format_input_output(['Columbia University', 'New York, NY, USA']))  # Columbia University, New York, NY, USA
print(format_input_output(['NYU', 'New York, New York, USA']))  # NYU, New York, New York, USA
print(format_input_output(['UC Berkeley', 'Berkeley, CA']))  # UC Berkeley, Berkeley, CA
print(format_input_output(['UIUC', 'Urbana, IL']))  # UIUC, Urbana, IL
print(format_input_output(['Temple University', 'Philadelphia, PA']))  # Temple University, Philadelphia, PA
print(format_input_output(['Harvard University', 'Cambridge, MA, USA']))  # Harvard University, Cambridge, MA, USA
print(format_input_output(['University of Connecticut', 'Storrs, CT, USA']))  # University of Connecticut, Storrs, CT, USA
print(format_input_output(['Drexel University', 'Philadelphia, PA']))  # Drexel University, Philadelphia, PA
print(format_input_output(['New Haven University', 'New Haven, CT, USA']))  # New Haven University, New Haven, CT, USA
print(format_input_output(['University of California, Santa Barbara', 'Santa Barbara, CA, USA']))  # University of California, Santa Barbara, Santa Barbara, CA, USA
