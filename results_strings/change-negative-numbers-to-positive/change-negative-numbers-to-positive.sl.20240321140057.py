# Prompt: if "-" present in the beginning of inputted expression, remove it
# Input: ['-%134']  Output: %134
# Input: ['500']  Output: 500
# Input: ['5.125']  Output: 5.125
# Input: ['-%43.00']  Output: %43.00

def remove_minus(input_str):
    if input_str[0] == '-':
        return input_str[1:]
    return input_str

# Test cases
print(remove_minus('-%134'))  # Output: %134
print(remove_minus('500'))    # Output: 500
print(remove_minus('5.125'))  # Output: 5.125
print(remove_minus('-%43.00'))  # Output: %43.00
