def return_second_input(input_str):
    input_list = input_str.split(', ')
    second_input = input_list[1]
    if "USA" not in second_input:
        return second_input + ', USA'
    return second_input

# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA

# Test cases
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Phialdelphia, PA, USA
print(return_second_input('UCLA, Los Angeles, CA'))  # Los Angeles, CA, USA
print(return_second_input('Cornell University, Ithaca, New York, USA'))  # Ithaca, NY, USA
print(return_second_input('Penn, Philadelphia, PA, USA'))  # Philadelphia, PA, USA
print(return_second_input('University of Maryland College Park, College Park, MD'))  # College Park, MD, USA
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))  # Ann Arbor, MI, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Berkeley, CA, USA
print(return_second_input('MIT, Cambridge, MA'))  # Cambridge, MA, USA
print(return_second_input('Rice University, Houston, TX'))  # Houston, TX, USA
print(return_second_input('Yale University, New Haven, CT, USA'))  # New Haven, CT, USA
print(return_second_input('Columbia University, New York, NY, USA'))  # New York, NY, USA
print(return_second_input('NYU, New York, New York, USA'))  # New York, NY, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Berkeley, CA, USA
print(return_second_input('UIUC, Urbana, IL'))  # Urbana, IL, USA
print(return_second_input('Temple University, Philadelphia, PA'))  # Philadelphia, PA, USA
print(return_second_input('Harvard University, Cambridge, MA, USA'))  # Cambridge, MA, USA
print(return_second_input('University of Connecticut, Storrs, CT, USA'))  # Storrs, CT, USA
print(return_second_input('Drexel University, Philadelphia, PA'))  # Philadelphia, PA, USA
print(return_second_input('New Haven University, New Haven, CT, USA'))  # New Haven, CT, USA
print(return_second_input('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Santa Barbara, CA, USA
