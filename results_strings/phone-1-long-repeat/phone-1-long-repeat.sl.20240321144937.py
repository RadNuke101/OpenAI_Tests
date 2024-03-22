def get_middle_number(input_str):
    nums = input_str.split('-')
    return nums[1]

# Prompt: return the three numbers between the "-", and given input as ['938-242-504'] output is 242
# Prompt: return the three numbers between the "-", and given input as ['308-916-545'] output is 916
# Prompt: return the three numbers between the "-", and given input as ['623-599-749'] output is 599
# Prompt: return the three numbers between the "-", and given input as ['981-424-843'] output is 424
# Prompt: return the three numbers between the "-", and given input as ['118-980-214'] output is 980
# Prompt: return the three numbers between the "-", and given input as ['244-655-094'] output is 655
# Prompt: return the three numbers between the "-", and given input as ['830-941-991'] output is 941
# Prompt: return the three numbers between the "-", and given input as ['911-186-562'] output is 186
# Prompt: return the three numbers between the "-", and given input as ['002-500-200'] output is 500
# Prompt: return the three numbers between the "-", and given input as ['113-860-034'] output is 860
# ... (repeated for all given inputs)

# Test the function with the provided inputs
print(get_middle_number('938-242-504'))  # Output: 242
print(get_middle_number('308-916-545'))  # Output: 916
print(get_middle_number('623-599-749'))  # Output: 599
print(get_middle_number('981-424-843'))  # Output: 424
print(get_middle_number('118-980-214'))  # Output: 980
print(get_middle_number('244-655-094'))  # Output: 655
print(get_middle_number('830-941-991'))  # Output: 941
print(get_middle_number('911-186-562'))  # Output: 186
print(get_middle_number('002-500-200'))  # Output: 500
print(get_middle_number('113-860-034'))  # Output: 860
# ... (repeated for all given inputs)
