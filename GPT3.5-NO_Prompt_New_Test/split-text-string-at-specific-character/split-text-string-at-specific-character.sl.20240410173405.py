# Start time: 2024-04-10 17:41:04.625556

'''
Prompt:
Given that input as ['011016_assignment.xlsx', '1'] output is 011016, input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, input as ['030116_cost.xlsx', '1'] output is 030116, input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        file_name = input_list[0].split('_')[1].split('.')[0]
        index = int(input_list[1])
        
        if index == 1:
            return file_name
        elif index == 2:
            return input_list[0].split('_')[1].split('.')[0] + '.' + input_list[0].split('_')[1].split('.')[1]
        else:
            return "Invalid index"
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('011016_assignment.xlsx,1'))
print(generated_function('011016_assignment.xlsx,2'))
print(generated_function('030116_cost.xlsx,1'))
print(generated_function('030116_cost.xlsx,2'))
print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx

# End time: 2024-04-10 17:41:07.064984
# Elapsed time in seconds: 2.4394040950001


# APPEND TEST SCRIPTS...
print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx


print(generated_function("011028_todosheet.xlsx", "1"))  ### Output: 011028
print(generated_function("030128_a.xlsx", "2"))  ### Output: a.xlsx
print(generated_function("030128_a.xlsx", "1"))  ### Output: 030128
print(generated_function("011028_todosheet.xlsx", "2"))  ### Output: todosheet.xlsx

# TEST SCRIPTS APPENDED!

