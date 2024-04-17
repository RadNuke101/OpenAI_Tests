# Start time: 2024-04-10 18:19:46.543130

'''
Prompt:
Given that input as ['spreadsheet', '1'] output is s, input as ['spreadsheet', '2'] output is p, input as ['spreadsheet', '3'] output is r, input as ['spreadsheet', '4'] output is e, input as ['spreadsheet', '5'] output is a, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        word, index = input_str.split(',')
        index = int(index)
        return word[index-1]
    except ValueError:
        return "Invalid input format"
    except IndexError:
        return "Index out of range"

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

# End time: 2024-04-10 18:19:48.319810
# Elapsed time in seconds: 1.776643219000107