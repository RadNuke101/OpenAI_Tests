# Prompt: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression
# Input: ['chang,amy'] -> Output: amy,chang
# Input: ['smith,bobby'] -> Output: bobby,smith
# Input: ['lennox,aaron'] -> Output: aaron,lennox

def rearrange_names(input_str):
    input_str = input_str[0]  # Extract the string from the list input
    names = input_str.split(',')
    output_str = names[1] + ',' + names[0]
    return output_str

# Test cases
print(rearrange_names(['chang,amy']))  # Output: amy,chang
print(rearrange_names(['smith,bobby']))  # Output: bobby,smith
print(rearrange_names(['lennox,aaron']))  # Output: aaron,lennox
amy,chang
bobby,smith
aaron,lennox
