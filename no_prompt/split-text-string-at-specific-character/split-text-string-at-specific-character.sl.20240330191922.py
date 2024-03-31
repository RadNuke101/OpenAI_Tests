# Start time: 2024-03-30 19:26:47.837312

# Content: Given that given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(file_name, option):
    try:
        if option == '1':
            output = file_name.split('_')[0]
        elif option == '2':
            output = file_name.split('_')[1].split('.')[0]
        else:
            raise ValueError("Invalid option. Please choose 1 or 2.")
    except IndexError:
        print("Invalid file name format. Please provide a valid file name.")
    except ValueError as e:
        print(e)
    else:
        return output

# Test cases
# Input: '011016_assignment.xlsx', '1'
# Output: 011016
print(extract_info('011016_assignment.xlsx', '1'))

# Input: '011016_assignment.xlsx', '2'
# Output: assignment.xlsx
print(extract_info('011016_assignment.xlsx', '2'))

# Input: '030116_cost.xlsx', '1'
# Output: 030116
print(extract_info('030116_cost.xlsx', '1'))

# Input: '030116_cost.xlsx', '2'
# Output: cost.xlsx
print(extract_info('030116_cost.xlsx', '2'))

# End time: 2024-03-30 19:26:51.041397
# Elapsed time in seconds: 3.203988500000378