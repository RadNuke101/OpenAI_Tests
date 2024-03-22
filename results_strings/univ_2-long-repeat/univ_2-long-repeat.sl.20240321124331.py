def add_country(input_str):
    inputs = input_str.split(', ')
    if "USA" not in inputs[1]:
        return inputs[0] + ', ' + inputs[1] + ', USA'
    return input_str

# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Connecticut', 'Storrs, CT, USA']
# Output: University of Connecticut, Storrs, CT, USA
# Input: ['Drexel University', 'Philadelphia, PA']
# Output: Drexel University, Philadelphia, PA, USA
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: UC Berkeley, Berkeley, CA, USA

# Test the function with the given inputs
print(add_country('University of Connecticut, Storrs, CT, USA'))
print(add_country('Drexel University, Philadelphia, PA'))
print(add_country('UC Berkeley, Berkeley, CA'))
