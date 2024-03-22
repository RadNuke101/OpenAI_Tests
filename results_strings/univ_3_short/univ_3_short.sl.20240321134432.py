# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA
# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Ithaca, New York, USA
# Input: ['Penn', 'Philadelphia, PA, USA']
# Output: Philadelphia, PA, USA
# Input: ['University of Maryland College Park', 'College Park, MD']
# Output: College Park, MD, USA
# Input: ['University of Michigan', 'Ann Arbor, MI, USA']
# Output: Ann Arbor, MI, USA

def return_second_input(input_list):
    second_input = input_list[1]
    if "USA" not in second_input:
        return second_input + ", USA"
    return second_input

# Test cases
print(return_second_input(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(return_second_input(['UCLA', 'Los Angeles, CA']))
print(return_second_input(['Cornell University', 'Ithaca, New York, USA']))
print(return_second_input(['Penn', 'Philadelphia, PA, USA']))
print(return_second_input(['University of Maryland College Park', 'College Park, MD']))
print(return_second_input(['University of Michigan', 'Ann Arbor, MI, USA']))
