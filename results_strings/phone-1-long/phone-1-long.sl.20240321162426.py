def get_middle_number(input_str):
    num_list = input_str.split('-')
    return num_list[1]

# Prompt: return the three numbers between the "-", 
# Input: ['938-242-504'], Output: 242
# Input: ['308-916-545'], Output: 916
# Input: ['623-599-749'], Output: 599

# Test cases
print(get_middle_number('938-242-504')) # Output: 242
print(get_middle_number('308-916-545')) # Output: 916
print(get_middle_number('623-599-749')) # Output: 599
