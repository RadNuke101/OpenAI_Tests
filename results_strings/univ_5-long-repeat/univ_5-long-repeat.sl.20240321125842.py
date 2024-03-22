def get_location(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    if 'USA' not in input_list[1]:
        input_list.append('USA')
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: 'University of California, Santa Barbara', 'Santa Barbara, CA, USA'
# Output: Santa Barbara, CA, USA

# Test cases
print(get_location('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Output: Santa Barbara, CA, USA
print(get_location('University of Connecticut, Storrs, CT, USA'))  # Output: Storrs, CT, USA
print(get_location('New Haven University, New Haven, CT, USA'))  # Output: New Haven, CT, USA
print(get_location('UIUC, Urbana, IL'))  # Output: Urbana, IL, USA
print(get_location('NYU, New York, New York, USA'))  # Output: New York, NY, USA
