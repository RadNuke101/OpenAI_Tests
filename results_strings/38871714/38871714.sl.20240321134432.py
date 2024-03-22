# Prompt: remove all instances of "<" and ">", 
# Input: ['This is a <string>, It should be <changed> to <a> number.']
# Output: This is a string, It should be changed to a number.
# Input: ['a < 4 and a > 0']
# Output: a  4 and a  0

def remove_angle_brackets(input_str):
    output_str = input_str.replace("<", "").replace(">", "")
    return output_str

# Test the function with the provided inputs
input1 = 'This is a <string>, It should be <changed> to <a> number.'
output1 = remove_angle_brackets(input1)
print(output1)

input2 = 'a < 4 and a > 0'
output2 = remove_angle_brackets(input2)
print(output2)
