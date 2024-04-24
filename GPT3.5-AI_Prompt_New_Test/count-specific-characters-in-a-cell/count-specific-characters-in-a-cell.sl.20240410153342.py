# Start time: 2024-04-10 15:48:17.483568

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of the name "Hannah" and a single letter in each row.

Summary for Output Column:
- The output column shows the count of occurrences of the letter specified in the input within the name "Hannah".

Relationship between Input and Output:
- The output count is based on how many times the specified letter appears in the name "Hannah" provided in the input. The relationship is direct and the output count is determined solely by the input letter and the name., and input as ['Hannah', 'n'] output is 2, input as ['Hannah', 'x'] output is 0, input as ['Hannah', 'N'] output is 0, input as ['Hannah', 'a'] output is 2, input as ['Hannah', 'h'] output is 1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(name, letter):
    # Count the occurrences of the letter in the name
    count = name.lower().count(letter.lower())
    return count

# Test cases
print(generated_function('Hannah', 'n'))  # Output: 2
print(generated_function('Hannah', 'x'))  # Output: 0
print(generated_function('Hannah', 'N'))  # Output: 0
print(generated_function('Hannah', 'a'))  # Output: 2
print(generated_function('Hannah', 'h'))  # Output: 1
print(generated_function("Hannah", "n"))  ## Output: 2
print(generated_function("Hannah", "x"))  ## Output: 0
print(generated_function("Hannah", "N"))  ## Output: 0
print(generated_function("Hannah", "a"))  ## Output: 2
print(generated_function("Hannah", "h"))  ## Output: 1

# End time: 2024-04-10 15:48:19.462106
# Elapsed time in seconds: 1.9784936309997647


# APPEND TEST SCRIPTS...
print(generated_function("Hannah", "n"))  ## Output: 2
print(generated_function("Hannah", "x"))  ## Output: 0
print(generated_function("Hannah", "N"))  ## Output: 0
print(generated_function("Hannah", "a"))  ## Output: 2
print(generated_function("Hannah", "h"))  ## Output: 1


print(generated_function("Mississippi", "x"))  ### Output: 0
print(generated_function("Mississippi", "l"))  ### Output: 0
print(generated_function("Mississippi", "M"))  ### Output: 1
print(generated_function("Mississippi", "i"))  ### Output: 4
print(generated_function("Mississippi", "p"))  ### Output: 2

# TEST SCRIPTS APPENDED!

