# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat'] 
# Output: true
def check_input(inputs):
    first_input = inputs.split()[0:2]
    second_input = inputs.split()[2]
    third_input = inputs.split()[3]
    fourth_input = inputs.split()[4]
    
    count = 0
    if second_input in first_input:
        count += 1
    if third_input in first_input:
        count += 1
    if fourth_input in first_input:
        count += 1
    
    return count == 1

# Test cases
print(check_input('yellow dog on green grass'))  # Output: true
print(check_input('warm gray sweater'))  # Output: false
print(check_input('blue neon signs'))  # Output: false
print(check_input('hot pink socks'))  # Output: true
print(check_input('deep black eyes'))  # Output: false
