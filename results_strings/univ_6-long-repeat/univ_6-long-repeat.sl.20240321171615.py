def get_location(input_str):
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
print(get_location('UC Berkeley, Berkeley, CA'))
print(get_location('University of Pennsylvania, Phialdelphia, PA, USA'))
print(get_location('UCLA, Los Angeles, CA'))
print(get_location('Cornell University, Ithaca, New York, USA'))
print(get_location('Penn, Philadelphia, PA, USA'))
print(get_location('University of Michigan, Ann Arbor, MI, USA'))
print(get_location('UC Berkeley, Berkeley, CA'))
print(get_location('MIT, Cambridge, MA'))
print(get_location('University of Pennsylvania, Phialdelphia, PA, USA'))
print(get_location('UCLA, Los Angeles, CA'))
print(get_location('University of Maryland College Park, College Park, MD'))
print(get_location('University of Michigan, Ann Arbor, MI, USA'))
print(get_location('UC Berkeley, Berkeley, CA'))
print(get_location('MIT, Cambridge, MA'))
print(get_location('Rice University, Houston, TX'))
print(get_location('Yale University, New Haven, CT, USA'))
print(get_location('Columbia University, New York, NY, USA'))
print(get_location('NYU, New York, New York, USA'))
print(get_location('Drexel University, Philadelphia, PA'))
print(get_location('UC Berkeley, Berkeley, CA'))
print(get_location('UIUC, Urbana, IL'))
print(get_location('Temple University, Philadelphia, PA'))
print(get_location('Harvard University, Cambridge, MA, USA'))
print(get_location('University of Connecticut, Storrs, CT, USA'))
print(get_location('Drexel University, Philadelphia, PA'))
print(get_location('NYU, New York, New York, USA'))
print(get_location('UIUC, Urbana, IL'))
print(get_location('New Haven University, New Haven, CT, USA'))
print(get_location('University of California, Santa Barbara, Santa Barbara, CA, USA'))
print(get_location('University of Connecticut, Storrs, CT, USA'))
