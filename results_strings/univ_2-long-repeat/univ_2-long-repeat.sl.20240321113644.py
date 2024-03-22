# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Connecticut', 'Storrs, CT, USA']
# Output: University of Connecticut, Storrs, CT, USA

def format_location(inputs):
    output = inputs[0] + ", " + inputs[1]
    if "USA" not in inputs[1]:
        output += ", USA"
    return output

# Test the function with the given input
print(format_location(['University of Connecticut', 'Storrs, CT, USA']))
