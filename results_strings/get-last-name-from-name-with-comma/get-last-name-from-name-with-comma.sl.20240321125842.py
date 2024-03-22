# Prompt: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression
# Input: ['chang,amy'] -> Output: amy,chang
# Input: ['smith,bobby'] -> Output: bobby,smith
# Input: ['lennox,aaron'] -> Output: aaron,lennox

def rearrange_names(input_str):
    parts = input_str.split(',')
    return parts[1] + ',' + parts[0]

# Test cases
print(rearrange_names('chang,amy'))  # Output: amy,chang
print(rearrange_names('smith,bobby'))  # Output: bobby,smith
print(rearrange_names('lennox,aaron'))  # Output: aaron,lennox
