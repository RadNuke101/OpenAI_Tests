# Prompt: if "C0" in expression, return the entire expression, else return second input (second column)
# Input: ['C0abc', 'def'] Output: C0abc
# Input: ['aabc', 'def'] Output: def
# Input: ['C0dd', 'qwe'] Output: C0dd
# Input: ['dd', 'qwe'] Output: qwe

def check_expression(input1, input2):
    if "C0" in input1:
        return input1
    else:
        return input2

# Test cases
print(check_expression('C0abc', 'def'))  # Output: C0abc
print(check_expression('aabc', 'def'))   # Output: def
print(check_expression('C0dd', 'qwe'))   # Output: C0dd
print(check_expression('dd', 'qwe'))     # Output: qwe
