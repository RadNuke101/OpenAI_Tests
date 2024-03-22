def second_input(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    if 'USA' not in input_list[1]:
        input_list.append('USA')
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

# Test cases
print(second_input('UC Berkeley, Berkeley, CA'))
print(second_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(second_input('Cornell University, Ithaca, New York, USA'))
print(second_input('Penn, Philadelphia, PA, USA'))
print(second_input('University of Michigan, Ann Arbor, MI, USA'))
print(second_input('UC Berkeley, Berkeley, CA'))
print(second_input('MIT, Cambridge, MA'))
print(second_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(second_input('UCLA, Los Angeles, CA'))
print(second_input('University of Maryland College Park, College Park, MD'))
print(second_input('University of Michigan, Ann Arbor, MI, USA'))
print(second_input('UC Berkeley, Berkeley, CA'))
print(second_input('MIT, Cambridge, MA'))
print(second_input('Rice University, Houston, TX'))
print(second_input('Yale University, New Haven, CT, USA'))
print(second_input('Columbia University, New York, NY, USA'))
print(second_input('NYU, New York, New York, USA'))
print(second_input('Drexel University, Philadelphia, PA'))
print(second_input('UC Berkeley, Berkeley, CA'))
print(second_input('UIUC, Urbana, IL'))
print(second_input('Temple University, Philadelphia, PA'))
print(second_input('Harvard University, Cambridge, MA, USA'))
print(second_input('University of Connecticut, Storrs, CT, USA'))
print(second_input('Drexel University, Philadelphia, PA'))
print(second_input('NYU, New York, New York, USA'))
print(second_input('UIUC, Urbana, IL'))
print(second_input('New Haven University, New Haven, CT, USA'))
print(second_input('University of California, Santa Barbara, CA, USA'))
print(second_input('University of Connecticut, Storrs, CT, USA'))
