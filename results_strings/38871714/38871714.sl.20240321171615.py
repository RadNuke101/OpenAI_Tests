# Prompt: remove all instances of "<" and ">", and given input as ['This is a <string>, It should be <changed> to <a> number.'] output is This is a string, It should be changed to a number., given input as ['a < 4 and a > 0'] output is a  4 and a  0

def remove_angle_brackets(input_str):
    output_str = input_str.replace('<', '').replace('>', '')
    return output_str

# Test cases
print(remove_angle_brackets('This is a <string>, It should be <changed> to <a> number.'))  # Output: This is a string, It should be changed to a number.
print(remove_angle_brackets('a < 4 and a > 0'))  # Output: a  4 and a  0
This is a string, It should be changed to a number.
a  4 and a  0
