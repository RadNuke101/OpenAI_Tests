# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: UCLA, Los Angeles, CA, USA
# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Cornell University, Ithaca, New York, USA
# Input: ['Penn', 'Philadelphia, PA, USA']
# Output: Penn, Philadelphia, PA, USA
# Input: ['University of Maryland College Park', 'College Park, MD']
# Output: University of Maryland College Park, College Park, MD, USA
# Input: ['University of Michigan', 'Ann Arbor, MI, USA']
# Output: University of Michigan, Ann Arbor, MI, USA

def format_location(input):
    output = input[0] + ', ' + input[1]
    if "USA" not in input[1]:
        output += ', USA'
    return output

# Test cases
print(format_location(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_location(['UCLA', 'Los Angeles, CA']))
print(format_location(['Cornell University', 'Ithaca, New York, USA']))
print(format_location(['Penn', 'Philadelphia, PA, USA']))
print(format_location(['University of Maryland College Park', 'College Park, MD']))
print(format_location(['University of Michigan', 'Ann Arbor, MI, USA']))
University of Pennsylvania, Phialdelphia, PA, USA
UCLA, Los Angeles, CA, USA
Cornell University, Ithaca, New York, USA
Penn, Philadelphia, PA, USA
University of Maryland College Park, College Park, MD, USA
University of Michigan, Ann Arbor, MI, USA
