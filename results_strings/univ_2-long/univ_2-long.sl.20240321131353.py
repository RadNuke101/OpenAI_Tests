# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_list):
    output = input_list[0] + ", " + input_list[1]
    if "USA" not in input_list[1]:
        output += ", USA"
    return output

# Test cases
print(format_input_output(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_input_output(['UCLA', 'Los Angeles, CA']))
print(format_input_output(['Cornell University', 'Ithaca, New York, USA']))
print(format_input_output(['Penn', 'Philadelphia, PA, USA']))
print(format_input_output(['University of Maryland College Park', 'College Park, MD']))
print(format_input_output(['University of Michigan', 'Ann Arbor, MI, USA']))
print(format_input_output(['UC Berkeley', 'Berkeley, CA']))
print(format_input_output(['MIT', 'Cambridge, MA']))
print(format_input_output(['Rice University', 'Houston, TX']))
print(format_input_output(['Yale University', 'New Haven, CT, USA']))
print(format_input_output(['Columbia University', 'New York, NY, USA']))
print(format_input_output(['NYU', 'New York, New York, USA']))
print(format_input_output(['UC Berkeley', 'Berkeley, CA']))
print(format_input_output(['UIUC', 'Urbana, IL']))
print(format_input_output(['Temple University', 'Philadelphia, PA']))
print(format_input_output(['Harvard University', 'Cambridge, MA, USA']))
print(format_input_output(['University of Connecticut', 'Storrs, CT, USA']))
print(format_input_output(['Drexel University', 'Philadelphia, PA']))
print(format_input_output(['New Haven University', 'New Haven, CT, USA']))
print(format_input_output(['University of California, Santa Barbara', 'Santa Barbara, CA, USA']))
University of Pennsylvania, Phialdelphia, PA, USA
UCLA, Los Angeles, CA, USA
Cornell University, Ithaca, New York, USA
Penn, Philadelphia, PA, USA
University of Maryland College Park, College Park, MD, USA
University of Michigan, Ann Arbor, MI, USA
UC Berkeley, Berkeley, CA, USA
MIT, Cambridge, MA, USA
Rice University, Houston, TX, USA
Yale University, New Haven, CT, USA
Columbia University, New York, NY, USA
NYU, New York, New York, USA
UC Berkeley, Berkeley, CA, USA
UIUC, Urbana, IL, USA
Temple University, Philadelphia, PA, USA
Harvard University, Cambridge, MA, USA
University of Connecticut, Storrs, CT, USA
Drexel University, Philadelphia, PA, USA
New Haven University, New Haven, CT, USA
University of California, Santa Barbara, Santa Barbara, CA, USA
