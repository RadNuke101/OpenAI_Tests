# Start time: 2024-04-10 13:03:30.086687

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if a number is present in the inputted expression, return true, else false, and input as ['A bird in the hand is worth 2 in the bush.'] output is true, input as ['A bird in the hand is worth two in the bush.'] output is false, input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Check if a number is present in the inputted expression
    if any(char.isdigit() for char in input_str):
        return True
    else:
        return False

# Test cases
print(generated_function('A bird in the hand is worth 2 in the bush.'))  # Output: True
print(generated_function('A bird in the hand is worth two in the bush.'))  # Output: False
print(generated_function('The 15 shortcuts you simply must know'))  # Output: True
print(generated_function("A bird in the hand is worth 2 in the bush."))  ## Output: true
print(generated_function("A bird in the hand is worth two in the bush."))  ## Output: false
print(generated_function("The 15 shortcuts you simply must know"))  ## Output: true

# End time: 2024-04-10 13:03:32.173938
# Elapsed time in seconds: 2.0872129279999854