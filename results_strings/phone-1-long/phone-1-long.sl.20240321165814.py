def get_middle_number(input_str):
    nums = input_str.split('-')
    return nums[1]

# Prompt: return the three numbers between the "-", 
# Input: ['938-242-504'] Output: 242
# Input: ['308-916-545'] Output: 916
# Input: ['623-599-749'] Output: 599
# Input: ['981-424-843'] Output: 424
# Input: ['118-980-214'] Output: 980
# Input: ['244-655-094'] Output: 655
# ... (additional inputs and outputs provided in the prompt)

# Test cases
print(get_middle_number('938-242-504')) # Output: 242
print(get_middle_number('308-916-545')) # Output: 916
print(get_middle_number('623-599-749')) # Output: 599
