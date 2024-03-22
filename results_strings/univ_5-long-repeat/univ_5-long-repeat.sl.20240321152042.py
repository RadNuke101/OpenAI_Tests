def process_input(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    if 'USA' not in input_list[1]:
        input_list.append('USA')
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

# Test cases
print(process_input('University of California, Santa Barbara, Santa Barbara, CA, USA'))
print(process_input('University of Connecticut, Storrs, CT, USA'))
print(process_input('New Haven University, New Haven, CT, USA'))
print(process_input('UIUC, Urbana, IL'))
print(process_input('Drexel University, Philadelphia, PA'))
print(process_input('NYU, New York, New York, USA'))
print(process_input('Harvard University, Cambridge, MA, USA'))
