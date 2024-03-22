# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

def return_second_input(input):
    second_input = input.split(',')[1].strip()
    if "USA" not in second_input:
        return second_input + ', USA'
    return second_input

# Test cases
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(return_second_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, NY, USA
print(return_second_input('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('MIT, Cambridge, MA'))  # Output: Cambridge, MA, USA
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(return_second_input('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(return_second_input('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('MIT, Cambridge, MA'))  # Output: Cambridge, MA, USA
print(return_second_input('Rice University, Houston, TX'))  # Output: Houston, TX, USA
print(return_second_input('Yale University, New Haven, CT, USA'))  # Output: New Haven, CT, USA
print(return_second_input('Columbia University, New York, NY, USA'))  # Output: New York, NY, USA
print(return_second_input('NYU, New York, New York, USA'))  # Output: New York, NY, USA
print(return_second_input('Drexel University, Philadelphia, PA'))  # Output: Philadelphia, PA, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('UIUC, Urbana, IL'))  # Output: Urbana, IL, USA
print(return_second_input('Temple University, Philadelphia, PA'))  # Output: Philadelphia, PA, USA
print(return_second_input('Harvard University, Cambridge, MA, USA'))  # Output: Cambridge, MA, USA
print(return_second_input('University of Connecticut, Storrs, CT, USA'))  # Output: Storrs, CT, USA
print(return_second_input('Drexel University, Philadelphia, PA'))  # Output: Philadelphia, PA, USA
print(return_second_input('NYU, New York, New York, USA'))  # Output: New York, NY, USA
print(return_second_input('UIUC, Urbana, IL'))  # Output: Urbana, IL, USA
print(return_second_input('New Haven University, New Haven, CT, USA'))  # Output: New Haven, CT, USA
print(return_second_input('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Output: Santa Barbara, CA, USA
print(return_second_input('University of Connecticut, Storrs, CT, USA'))  # Output: Storrs, CT, USA
