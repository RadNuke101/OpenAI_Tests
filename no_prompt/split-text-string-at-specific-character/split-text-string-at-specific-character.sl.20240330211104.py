# Start time: 2024-03-30 21:19:27.792011

# Content: Given that given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(file_name, option):
    try:
        file_name = file_name.split('_')[0]
        if option == '1':
            return file_name
        elif option == '2':
            return file_name.split('_')[1] + '.xlsx'
        else:
            return "Invalid option. Please choose either '1' or '2'."
    except Exception as e:
        return "Error: " + str(e)

# Test cases
# print(extract_info('011016_assignment.xlsx', '1'))  # Output: 011016
# print(extract_info('011016_assignment.xlsx', '2'))  # Output: assignment.xlsx
# print(extract_info('030116_cost.xlsx', '1'))  # Output: 030116
# print(extract_info('030116_cost.xlsx', '2'))  # Output: cost.xlsx

# End time: 2024-03-30 21:19:29.875139
# Elapsed time in seconds: 2.083081262999258