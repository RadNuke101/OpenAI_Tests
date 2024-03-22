# Prompt: if "-" present in the beginning of inputted expression (first column), remove it
# Input: ['-%134'] -> Output: %134
# Input: ['500'] -> Output: 500
# Input: ['5.125'] -> Output: 5.125
# Input: ['-%43.00'] -> Output: %43.00

def remove_dash(input_str):
    if input_str.startswith('-'):
        return input_str[1:]
    return input_str

# Test cases
print(remove_dash('-%134'))  # Output: %134
print(remove_dash('500'))     # Output: 500
print(remove_dash('5.125'))   # Output: 5.125
print(remove_dash('-%43.00')) # Output: %43.00
