# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def process_input(input):
    if "New York" in input:
        return input.replace("New York", "NY")
    elif "USA" not in input:
        return input + ", USA"
    else:
        return input

# Test cases
print(process_input('University of Pennsylvania, Phialdelphia, PA, USA'))
print(process_input('UCLA, Los Angeles, CA'))
print(process_input('Cornell University, Ithaca, New York, USA'))
print(process_input('Penn, Philadelphia, PA, USA'))
print(process_input('University of Maryland College Park, College Park, MD'))
print(process_input('University of Michigan, Ann Arbor, MI, USA'))
print(process_input('Columbia University, New York, NY, USA'))
print(process_input('NYU, New York, New York, USA'))
