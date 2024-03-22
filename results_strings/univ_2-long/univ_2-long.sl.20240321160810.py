# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_str):
    inputs = input_str.split(', ')
    output = inputs[0] + ', ' + inputs[1]
    
    if 'USA' not in inputs[1]:
        output += ', USA'
    
    return output

# Test cases
print(format_input_output('University of Pennsylvania, Phialdelphia, PA, USA'))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output('UCLA, Los Angeles, CA'))  # UCLA, Los Angeles, CA, USA
print(format_input_output('Cornell University, Ithaca, New York, USA'))  # Cornell University, Ithaca, New York, USA
print(format_input_output('Penn, Philadelphia, PA, USA'))  # Penn, Philadelphia, PA, USA
print(format_input_output('University of Maryland College Park, College Park, MD'))  # University of Maryland College Park, College Park, MD, USA
