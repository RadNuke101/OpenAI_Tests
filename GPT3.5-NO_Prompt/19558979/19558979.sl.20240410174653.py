# Start time: 2024-04-10 17:56:59.087805

'''
Prompt:
Given that input as ['spreadsheet', '1'] output is s, input as ['spreadsheet', '2'] output is p, input as ['spreadsheet', '3'] output is r, input as ['spreadsheet', '4'] output is e, input as ['spreadsheet', '5'] output is a, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        word = input_list[0]
        index = int(input_list[1])
        return word[index-1]
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
print(generated_function('spreadsheet,1'))
print(generated_function('spreadsheet,2'))
print(generated_function('spreadsheet,3'))
print(generated_function('spreadsheet,4'))
print(generated_function('spreadsheet,5'))
print(generated_function("spreadsheet", "1"))  ## Output: s
print(generated_function("spreadsheet", "2"))  ## Output: p
print(generated_function("spreadsheet", "3"))  ## Output: r
print(generated_function("spreadsheet", "4"))  ## Output: e
print(generated_function("spreadsheet", "5"))  ## Output: a

# End time: 2024-04-10 17:57:00.769464
# Elapsed time in seconds: 1.6816174729999602