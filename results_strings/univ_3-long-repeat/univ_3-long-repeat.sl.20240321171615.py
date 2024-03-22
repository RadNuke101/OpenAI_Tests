# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

def process_input(input_str):
    input_list = input_str.split(', ')
    if 'USA' not in input_list[1]:
        return input_list[1] + ', USA'
    return input_list[1]

# Test the function with the provided inputs
print(process_input('UC Berkeley, Berkeley, CA'))
print(process_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(process_input('Cornell University, Ithaca, New York, USA'))
print(process_input('Penn, Philadelphia, PA, USA'))
print(process_input('University of Michigan, Ann Arbor, MI, USA'))
print(process_input('UC Berkeley, Berkeley, CA'))
print(process_input('MIT, Cambridge, MA'))
print(process_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(process_input('UCLA, Los Angeles, CA'))
print(process_input('University of Maryland College Park, College Park, MD'))
print(process_input('University of Michigan, Ann Arbor, MI, USA'))
print(process_input('UC Berkeley, Berkeley, CA'))
print(process_input('MIT, Cambridge, MA'))
print(process_input('Rice University, Houston, TX'))
print(process_input('Yale University, New Haven, CT, USA'))
print(process_input('Columbia University, New York, NY, USA'))
print(process_input('NYU, New York, New York, USA'))
print(process_input('Drexel University, Philadelphia, PA'))
print(process_input('UC Berkeley, Berkeley, CA'))
print(process_input('UIUC, Urbana, IL'))
print(process_input('Temple University, Philadelphia, PA'))
print(process_input('Harvard University, Cambridge, MA, USA'))
print(process_input('University of Connecticut, Storrs, CT, USA'))
print(process_input('Drexel University, Philadelphia, PA'))
print(process_input('NYU, New York, New York, USA'))
print(process_input('UIUC, Urbana, IL'))
print(process_input('New Haven University, New Haven, CT, USA'))
print(process_input('University of California, Santa Barbara, Santa Barbara, CA, USA'))
print(process_input('University of Connecticut, Storrs, CT, USA'))
