# Prompt: return everything after the space in the inputted expression
# Input: 'year= 2016'
# Output: '2016'

def get_output(input_str):
    return input_str.split(' ')[1]

# Test cases
print(get_output('year= 2016'))  # Output: '2016'
print(get_output('make= subaru'))  # Output: 'subaru'
print(get_output('model= outback wagon'))  # Output: 'outback wagon'
print(get_output('fuel economy= 25/33'))  # Output: '25/33'
