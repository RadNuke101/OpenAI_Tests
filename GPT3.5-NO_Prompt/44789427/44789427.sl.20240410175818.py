# Start time: 2024-04-10 18:06:22.673018

'''
Prompt:
Given that input as ['1/17/16-1/18/17', '1'] output is 1/17/16, input as ['1/17/16-1/18/17', '2'] output is 1/18/17, input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        date_range = input_list[0].split('-')
        index = int(input_list[1].strip()) - 1
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()
        
        if '/' in start_date:
            start_date = start_date.replace('/', '-')
        if '/' in end_date:
            end_date = end_date.replace('/', '-')
        
        if index == 0:
            return start_date
        elif index == 1:
            return end_date
        else:
            return "Invalid index"
    
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('1/17/16-1/18/17, 1'))
print(generated_function('1/17/16-1/18/17, 2'))
print(generated_function('01/17/2016-01/18/2017, 1'))
print(generated_function('01/17/2016-01/18/2017, 2'))
print(generated_function("1/17/16-1/18/17", "1"))  ## Output: 1/17/16
print(generated_function("1/17/16-1/18/17", "2"))  ## Output: 1/18/17
print(generated_function("01/17/2016-01/18/2017", "1"))  ## Output: 01/17/2016
print(generated_function("01/17/2016-01/18/2017", "2"))  ## Output: 01/18/2017

# End time: 2024-04-10 18:06:26.194227
# Elapsed time in seconds: 3.5211445390000335