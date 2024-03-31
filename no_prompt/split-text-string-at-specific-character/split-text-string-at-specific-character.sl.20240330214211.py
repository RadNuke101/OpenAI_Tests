# Start time: 2024-03-30 21:51:10.687351

# Content: Given that given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(file_name, option):
    try:
        file_name = file_name.split('_')
        if option == '1':
            output = file_name[0]
        elif option == '2':
            output = '_'.join(file_name[1:])
        else:
            raise ValueError("Option must be '1' or '2'")
    except IndexError:
        output = "Invalid file name format"
    except ValueError as e:
        output = str(e)
    
    return output

# Test cases
print(extract_info('011016_assignment.xlsx', '1'))  # Output: 011016
print(extract_info('011016_assignment.xlsx', '2'))  # Output: assignment.xlsx
print(extract_info('030116_cost.xlsx', '1'))  # Output: 030116
print(extract_info('030116_cost.xlsx', '2'))  # Output: cost.xlsx

# End time: 2024-03-30 21:51:14.334168
# Elapsed time in seconds: 3.646707445001084