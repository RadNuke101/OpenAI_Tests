# Prompt: remove all instances of "<" and ">", 
# Input: ['This is a <string>, It should be <changed> to <a> number.']
# Output: This is a string, It should be changed to a number.

def remove_symbols(input_str):
    output_str = input_str.replace("<", "").replace(">", "")
    return output_str

# Test cases
print(remove_symbols('This is a <string>, It should be <changed> to <a> number.'))  # Output: This is a string, It should be changed to a number.
print(remove_symbols('a < 4 and a > 0'))  # Output: a  4 and a  0
