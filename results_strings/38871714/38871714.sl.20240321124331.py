# Prompt: remove all instances of "<" and ">", and given input as ['This is a <string>, It should be <changed> to <a> number.'] output is This is a string, It should be changed to a number., given input as ['a < 4 and a > 0'] output is a  4 and a  0

def remove_symbols(input_str):
    output_str = input_str.replace('<', '').replace('>', '')
    return output_str

# Test cases
input1 = 'This is a <string>, It should be <changed> to <a> number.'
output1 = remove_symbols(input1)
print(output1)  # This is a string, It should be changed to a number.

input2 = 'a < 4 and a > 0'
output2 = remove_symbols(input2)
print(output2)  # a  4 and a  0
