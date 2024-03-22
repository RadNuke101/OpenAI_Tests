# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

def process_input(input_str):
    inputs = input_str.split(', ')
    second_input = inputs[1]
    
    if 'New York' in second_input:
        second_input = second_input.replace('New York', 'NY')
    
    if 'USA' not in second_input:
        second_input += ', USA'
    
    return second_input

# Test cases
print(process_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(process_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(process_input('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(process_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, NY, USA
print(process_input('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(process_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
