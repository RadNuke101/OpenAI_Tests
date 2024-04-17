# Start time: 2024-04-10 14:49:43.614587

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (Qualitative Data):
- The input column 1 contains a combination of last name and first name separated by a comma.
- The names in the input column 1 are in the format "Last Name, First Name".

Summary for Input Column 2 (Qualitative Data):
- The input column 2 contains numerical values representing different categories.

Summary for Output Column (Qualitative Data):
- The output column contains the first or last name extracted from the input column 1 based on the numerical value in input column 2.

Relationship between Input and Output:
- The output column displays either the first name or last name from the input column 1 based on the numerical value in input column 2.
- When the numerical value is '1', the output displays the first name.
- When the numerical value is '2', the output displays the last name.
- The relationship between input and output is that the output is determined by the numerical value in the input column 2, which dictates whether the first name or last name is displayed., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str, num_str):
    # Split the input string into last name and first name
    last_name, first_name = input_str.split(',')
    
    # Check the numerical value to determine output
    if num_str == '1':
        return first_name.strip()
    elif num_str == '2':
        return last_name.strip()

# Test cases
print(generated_function('Chang,Amy', '1'))  # Output: Amy
print(generated_function('Chang,Amy', '2'))  # Output: Chang
print(generated_function('smith,bobby', '2'))  # Output: smith
print(generated_function('smith,bobby', '1'))  # Output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-10 14:49:45.970897
# Elapsed time in seconds: 2.356241872000055