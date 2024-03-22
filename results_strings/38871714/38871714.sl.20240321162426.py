# Prompt: remove all instances of "<" and ">", 
# Input: ['This is a <string>, It should be <changed> to <a> number.']
# Output: This is a string, It should be changed to a number.

def remove_brackets(input_str):
    output_str = input_str.replace('<', '').replace('>', '')
    return output_str

# Test cases
print(remove_brackets('This is a <string>, It should be <changed> to <a> number.'))  # Output: This is a string, It should be changed to a number.
print(remove_brackets('a < 4 and a > 0'))  # Output: a  4 and a  0
