# Start time: 2024-04-10 15:35:12.515461

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1:
- The input column 1 contains a list of names in the format "Lastname,Firstname".
- The names in the input column 1 are diverse and varied.

Summary for Input Column 2:
- The input column 2 contains numerical values representing different choices.
- The values in the input column 2 are limited to the numbers 1 and 2.

Summary for Output Column:
- The output column contains the first or last name based on the choice made in input column 2.
- The output column displays a clear relationship between the input choices and the corresponding names.

Relationship between Input and Output:
- The output column displays the first or last name based on the choice made in input column 2.
- When input column 2 is '1', the output column displays the first name.
- When input column 2 is '2', the output column displays the last name.
- The relationship between the input choices and the output names is straightforward and follows a consistent pattern., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(name_input, choice_input):
    # Split the name_input into last name and first name
    last_name, first_name = name_input.split(',')
    
    # Check the choice_input and return the corresponding name
    if choice_input == '1':
        return first_name
    elif choice_input == '2':
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

# End time: 2024-04-10 15:35:15.323433
# Elapsed time in seconds: 2.8079172650004693