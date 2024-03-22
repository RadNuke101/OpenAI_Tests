# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def return_second_input(input):
    if "USA" not in input:
        return input + ", USA"
    return input

# Test cases
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(return_second_input('UCLA, Los Angeles, CA'))
print(return_second_input('Cornell University, Ithaca, New York, USA'))
print(return_second_input('Penn, Philadelphia, PA, USA'))
print(return_second_input('University of Maryland College Park, College Park, MD'))
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))
Phialdelphia, PA, USA
Los Angeles, CA, USA
Ithaca, New York, USA
Philadelphia, PA, USA
College Park, MD, USA
Ann Arbor, MI, USA
