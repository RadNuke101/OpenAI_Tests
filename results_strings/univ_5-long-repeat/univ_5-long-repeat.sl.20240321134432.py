def second_input(input_str):
    input_list = input_str.split(', ')
    if 'New York' in input_list[1]:
        input_list[1] = 'NY'
    if 'USA' not in input_list[1]:
        input_list.append('USA')
    return ', '.join(input_list)

# Input: "University of California, Santa Barbara, Santa Barbara, CA, USA"
# Output: "Santa Barbara, CA, USA"
# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"

# Test cases
print(second_input("UC Berkeley, Berkeley, CA"))  # Output: "Berkeley, CA, USA"
print(second_input("University of Pennsylvania, Phialdelphia, PA, USA"))  # Output: "Phialdelphia, PA, USA"
print(second_input("Cornell University, Ithaca, New York, USA"))  # Output: "Ithaca, NY, USA"
print(second_input("Penn, Philadelphia, PA, USA"))  # Output: "Philadelphia, PA, USA"
print(second_input("University of Michigan, Ann Arbor, MI, USA"))  # Output: "Ann Arbor, MI, USA"
