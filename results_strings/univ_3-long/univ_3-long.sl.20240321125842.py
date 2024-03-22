# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA

def return_second_input(input_list):
    second_input = input_list.split(',')[1].strip()
    if "USA" not in second_input:
        return second_input + ', USA'
    return second_input

# Test cases
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(return_second_input('UCLA, Los Angeles, CA'))
print(return_second_input('Cornell University, Ithaca, New York, USA'))
print(return_second_input('Penn, Philadelphia, PA, USA'))
print(return_second_input('University of Maryland College Park, College Park, MD'))
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))
print(return_second_input('UC Berkeley, Berkeley, CA'))
print(return_second_input('MIT, Cambridge, MA'))
print(return_second_input('Rice University, Houston, TX'))
print(return_second_input('Yale University, New Haven, CT, USA'))
print(return_second_input('Columbia University, New York, NY, USA'))
print(return_second_input('NYU, New York, New York, USA'))
print(return_second_input('UC Berkeley, Berkeley, CA'))
print(return_second_input('UIUC, Urbana, IL'))
print(return_second_input('Temple University, Philadelphia, PA'))
print(return_second_input('Harvard University, Cambridge, MA, USA'))
print(return_second_input('University of Connecticut, Storrs, CT, USA'))
print(return_second_input('Drexel University, Philadelphia, PA'))
print(return_second_input('New Haven University, New Haven, CT, USA'))
print(return_second_input('University of California, Santa Barbara, Santa Barbara, CA, USA'))
