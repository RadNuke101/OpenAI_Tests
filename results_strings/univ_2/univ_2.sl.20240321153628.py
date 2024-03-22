# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA
def format_input(input):
    output = input[0] + ', ' + input[1]
    if 'USA' not in input[1]:
        output += ', USA'
    return output

# Test cases
print(format_input(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_input(['UCLA', 'Los Angeles, CA']))
print(format_input(['Cornell University', 'Ithaca, New York, USA']))
print(format_input(['Penn', 'Philadelphia, PA, USA']))
print(format_input(['University of Maryland College Park', 'College Park, MD']))
print(format_input(['University of Michigan', 'Ann Arbor, MI, USA']))
University of Pennsylvania, Phialdelphia, PA, USA
UCLA, Los Angeles, CA, USA
Cornell University, Ithaca, New York, USA
Penn, Philadelphia, PA, USA
University of Maryland College Park, College Park, MD, USA
University of Michigan, Ann Arbor, MI, USA
