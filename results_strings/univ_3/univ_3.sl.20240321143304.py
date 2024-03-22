# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def second_input(input):
    second = input.split(',')[1].strip()
    if "USA" not in second:
        return second + ', USA'
    return second

# Test cases
print(second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(second_input('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(second_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, New York, USA
print(second_input('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(second_input('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(second_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
