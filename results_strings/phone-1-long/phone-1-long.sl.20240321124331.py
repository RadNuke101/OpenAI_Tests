def get_middle_number(input_str):
    input_str = input_str.replace('-', '')
    return input_str[3:6]

# Prompt: return the three numbers between the "-", 
# Input: ['938-242-504'] Output: 242
# Input: ['308-916-545'] Output: 916
# Input: ['623-599-749'] Output: 599
# Input: ['981-424-843'] Output: 424
# Input: ['118-980-214'] Output: 980

# Test cases
print(get_middle_number('938-242-504')) # Output: 242
print(get_middle_number('308-916-545')) # Output: 916
print(get_middle_number('623-599-749')) # Output: 599
print(get_middle_number('981-424-843')) # Output: 424
print(get_middle_number('118-980-214')) # Output: 980
