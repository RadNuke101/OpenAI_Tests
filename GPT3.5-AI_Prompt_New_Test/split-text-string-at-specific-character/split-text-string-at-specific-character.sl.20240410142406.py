# Start time: 2024-04-10 14:35:03.507539

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:

- Input column 1: The input column data consists of file names in the format 'mmddyy_filename.xlsx'. The first part represents the date in the format mmddyy.

- Input column 2: The input column data consists of numbers indicating different parts of the file name.

Summary for output column data:

- Output column: The output column data consists of the extracted parts of the file name based on the numbers provided in the input column. For example, if the number is 1, the output is the date part of the file name. If the number is 2, the output is the filename part of the file name.

Relationship between input and output:

The relationship between the input and output columns is that the output column is derived from the input column based on the number provided. The number determines which part of the file name should be extracted and displayed in the output column. This relationship allows for easy extraction of specific information from the file names provided in the input column., and input as ['011016_assignment.xlsx', '1'] output is 011016, input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, input as ['030116_cost.xlsx', '1'] output is 030116, input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to extract parts of the file name based on the number provided
def generated_function(file_name, number):
    # Split the file name into date and filename parts
    date_part, filename_part = file_name.split('_')
    
    # Check the number provided and return the corresponding part of the file name
    if number == '1':
        return date_part
    elif number == '2':
        return filename_part

# Test cases
print(generated_function('011016_assignment.xlsx', '1'))  # Output: 011016
print(generated_function('011016_assignment.xlsx', '2'))  # Output: assignment.xlsx
print(generated_function('030116_cost.xlsx', '1'))  # Output: 030116
print(generated_function('030116_cost.xlsx', '2'))  # Output: cost.xlsx
print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx

# End time: 2024-04-10 14:35:06.342326
# Elapsed time in seconds: 2.8347270829999616


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

