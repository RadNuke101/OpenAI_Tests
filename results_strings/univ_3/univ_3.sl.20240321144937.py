# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def second_input(input):
    if "USA" not in input:
        return input + ", USA"
    else:
        return input

# Test cases
print(second_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(second_input('UCLA, Los Angeles, CA'))
print(second_input('Cornell University, Ithaca, New York, USA'))
print(second_input('Penn, Philadelphia, PA, USA'))
print(second_input('University of Maryland College Park, College Park, MD'))
print(second_input('University of Michigan, Ann Arbor, MI, USA'))
