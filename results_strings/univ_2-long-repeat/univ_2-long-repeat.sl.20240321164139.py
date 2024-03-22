# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"

def format_location(input_str):
    inputs = input_str.split(', ')
    output = inputs[0] + ', ' + inputs[1]
    
    if 'USA' not in inputs[1]:
        output += ', USA'
    
    return output

# Test cases
print(format_location('UC Berkeley, Berkeley, CA')) # Output: UC Berkeley, Berkeley, CA, USA
print(format_location('University of Pennsylvania, Phialdelphia, PA, USA')) # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(format_location('UCLA, Los Angeles, CA')) # Output: UCLA, Los Angeles, CA, USA
print(format_location('Cornell University, Ithaca, New York, USA')) # Output: Cornell University, Ithaca, New York, USA
print(format_location('Penn, Philadelphia, PA, USA')) # Output: Penn, Philadelphia, PA, USA
print(format_location('University of Michigan, Ann Arbor, MI, USA')) # Output: University of Michigan, Ann Arbor, MI, USA
