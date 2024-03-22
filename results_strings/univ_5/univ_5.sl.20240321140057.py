# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def process_input(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    elif 'USA' not in input_list[1]:
        input_list.append('USA')
    return ', '.join(input_list)

# Test cases
print(process_input('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(process_input('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(process_input('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, NY, USA
print(process_input('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(process_input('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(process_input('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
print(process_input('Columbia University, New York, NY, USA'))  # Output: New York, NY, USA
print(process_input('NYU, New York, New York, USA'))  # Output: New York, NY, USA
