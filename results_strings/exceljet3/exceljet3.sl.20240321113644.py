# Prompt: return everything after the space in the inputted expression
# Input: 'year= 2016'
# Output: '2016'

def get_after_space(input_str):
    return input_str.split(' ')[1]

# Test cases
print(get_after_space('year= 2016'))  # Output: '2016'
print(get_after_space('make= subaru'))  # Output: 'subaru'
print(get_after_space('model= outback wagon'))  # Output: 'outback wagon'
print(get_after_space('fuel economy= 25/33'))  # Output: '25/33'
