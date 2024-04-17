# Start time: 2024-04-10 14:25:19.375020

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1:
- The input column 1 consists of last names followed by first names separated by a comma.
- The names in the input column are in the format Last Name, First Name.

Summary for Input Column 2:
- The input column 2 consists of numerical values representing a choice or option.

Summary for Output Column:
- The output column consists of first names or last names based on the choice made in input column 2.
- When the choice is '1', the output is the first name.
- When the choice is '2', the output is the last name.

Relationship between Input and Output:
- The relationship between the input and output is that the choice made in input column 2 determines whether the output will be the first name or last name from input column 1.
- When the choice is '1', the output is the first name.
- When the choice is '2', the output is the last name.
- The input column provides the full name, and the choice in input column 2 determines which part of the name is selected for the output., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name, choice):
    # Split the name into last name and first name
    last_name, first_name = name.split(',')

    # Check the choice and return the corresponding name
    if choice == '1':
        return first_name.strip()
    elif choice == '2':
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

# End time: 2024-04-10 14:25:21.613780
# Elapsed time in seconds: 2.2387145809999964