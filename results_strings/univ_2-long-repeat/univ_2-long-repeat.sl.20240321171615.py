# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: University of California, Santa Barbara, Santa Barbara, CA, USA

def format_location(input):
    output = input[0] + ', ' + input[1]
    if 'USA' not in input[1]:
        output += ', USA'
    return output

# Test the function
print(format_location(['University of California, Santa Barbara', 'Santa Barbara, CA, USA']))
