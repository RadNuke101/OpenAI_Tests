def add_country(input_str):
    inputs = input_str.split(', ')
    if 'USA' not in inputs[1]:
        return inputs[0] + ', ' + inputs[1] + ', USA'
    return input_str

# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Connecticut', 'Storrs, CT, USA']
# Output: University of Connecticut, Storrs, CT, USA
