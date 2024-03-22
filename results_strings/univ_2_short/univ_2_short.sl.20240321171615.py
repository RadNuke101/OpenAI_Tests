def format_location(input):
    if "USA" not in input[1]:
        return input[0] + ", " + input[1] + ", USA"
    else:
        return input[0] + ", " + input[1]

# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA
# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
