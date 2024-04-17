# Start time: 2024-04-10 18:03:00.257687

'''
Prompt:
Given that input as ['C0abc', 'def'] output is C0abc, input as ['aabc', 'def'] output is def, input as ['C0dd', 'qwe'] output is C0dd, input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        first_str = input_list[0].strip()
        second_str = input_list[1].strip()

        if first_str[0].isupper():
            return first_str
        else:
            return second_str
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('C0abc, def'))
print(generated_function('aabc, def'))
print(generated_function('C0dd, qwe'))
print(generated_function('dd, qwe'))
print(generated_function("C0abc", "def"))  ## Output: C0abc
print(generated_function("aabc", "def"))  ## Output: def
print(generated_function("C0dd", "qwe"))  ## Output: C0dd
print(generated_function("dd", "qwe"))  ## Output: qwe

# End time: 2024-04-10 18:03:02.156953
# Elapsed time in seconds: 1.899230747999809