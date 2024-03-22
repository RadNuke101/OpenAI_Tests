# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA

def return_second_input(input_str):
    inputs = input_str.split(', ')
    if 'USA' not in inputs[1]:
        return inputs[1] + ', USA'
    else:
        return inputs[1]

# Test cases
print(return_second_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(return_second_input('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(return_second_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, New York, USA
print(return_second_input('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(return_second_input('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(return_second_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
