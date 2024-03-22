def process_input(input_str):
    input_list = input_str.split(', ')
    second_input = input_list[1]
    
    if "New York" in second_input:
        second_input = second_input.replace("New York", "NY")
    
    if "USA" not in second_input:
        second_input += ", USA"
    
    return second_input

# Prompt: return the second input, but if it contains "New York", replace it with "NY". If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA

# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA

# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Ithaca, NY, USA

# Add more test cases as needed

# Test cases
print(process_input("University of Pennsylvania, Phialdelphia, PA, USA"))  # Phialdelphia, PA, USA
print(process_input("UCLA, Los Angeles, CA"))  # Los Angeles, CA, USA
print(process_input("Cornell University, Ithaca, New York, USA"))  # Ithaca, NY, USA
