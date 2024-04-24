# Start time: 2024-04-10 15:56:21.417691

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (['Chang,Amy', 'smith,bobby']):
- The input column 1 consists of last name, first name pairs.
- The names in the input column 1 are in the format "last name, first name".

Summary for Input Column 2 (['1', '2', '2', '1']):
- The input column 2 consists of numerical values representing different categories.

Summary for Output Column (['Amy', 'Chang', 'smith', 'bobby']):
- The output column consists of first names and last names extracted from the input column 1.
- The output column contains a mix of first names and last names.

Relationship between Input and Output:
- The output column seems to alternate between first names and last names based on the input column 2 values.
- When input column 2 is '1', the output is a first name.
- When input column 2 is '2', the output is a last name.
- The relationship between input and output suggests that the input column 2 determines whether the output will be a first name or a last name., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str, category):
    # Split the input string into last name and first name
    last_name, first_name = input_str.split(',')
    
    # Check the category value to determine the output
    if category == '1':
        return first_name
    elif category == '2':
        return last_name

# Test cases
print(generated_function('Chang,Amy', '1'))  # Output: Amy
print(generated_function('Chang,Amy', '2'))  # Output: Chang
print(generated_function('smith,bobby', '2'))  # Output: smith
print(generated_function('smith,bobby', '1'))  # Output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-10 15:56:23.364637
# Elapsed time in seconds: 1.946912971000529


# APPEND TEST SCRIPTS...
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby


print(generated_function("parker,olivia", "1"))  ### Output: olivia
print(generated_function("parker,olivia", "2"))  ### Output: parker
print(generated_function("Turner,Jackson", "2"))  ### Output: Turner
print(generated_function("Turner,Jackson", "1"))  ### Output: Jackson

# TEST SCRIPTS APPENDED!

