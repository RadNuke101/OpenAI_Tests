def get_middle_number(input_str):
    nums = input_str.split('-')
    return nums[1]

# Prompt: return the three numbers between the "-", and given input as ['938-242-504'] output is 242
# Input: '938-242-504'
# Output: '242'

# Test cases
print(get_middle_number('938-242-504'))  # Output: 242
print(get_middle_number('308-916-545'))  # Output: 916
print(get_middle_number('623-599-749'))  # Output: 599
print(get_middle_number('981-424-843'))  # Output: 424
print(get_middle_number('118-980-214'))  # Output: 980
print(get_middle_number('244-655-094'))  # Output: 655
print(get_middle_number('830-941-991'))  # Output: 941
print(get_middle_number('911-186-562'))  # Output: 186
