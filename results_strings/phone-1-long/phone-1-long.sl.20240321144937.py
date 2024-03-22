def get_middle_number(input_str):
    nums = input_str.split('-')
    return nums[1]

# Prompt: return the three numbers between the "-", 
# Input: ['938-242-504'], Output: 242
# Input: ['308-916-545'], Output: 916
# Input: ['623-599-749'], Output: 599
# Input: ['981-424-843'], Output: 424
# Input: ['118-980-214'], Output: 980
# Input: ['244-655-094'], Output: 655
# Input: ['830-941-991'], Output: 941
# Input: ['911-186-562'], Output: 186
# Input: ['002-500-200'], Output: 500
# Input: ['113-860-034'], Output: 860
# Add more test cases as needed

# Test cases
print(get_middle_number('938-242-504')) # Output: 242
print(get_middle_number('308-916-545')) # Output: 916
print(get_middle_number('623-599-749')) # Output: 599
print(get_middle_number('981-424-843')) # Output: 424
print(get_middle_number('118-980-214')) # Output: 980
print(get_middle_number('244-655-094')) # Output: 655
print(get_middle_number('830-941-991')) # Output: 941
print(get_middle_number('911-186-562')) # Output: 186
print(get_middle_number('002-500-200')) # Output: 500
print(get_middle_number('113-860-034')) # Output: 860
