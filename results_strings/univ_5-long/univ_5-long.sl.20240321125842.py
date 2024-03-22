def process_input(input_str):
    input_list = input_str.split(', ')
    if "New York" in input_list[1]:
        input_list[1] = "NY, USA"
    else:
        input_list[1] += ', USA'
    return ', '.join(input_list)

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA

# Test cases
print(process_input("University of Pennsylvania, Phialdelphia, PA, USA"))  # Phialdelphia, PA, USA
print(process_input("UCLA, Los Angeles, CA"))  # Los Angeles, CA, USA
