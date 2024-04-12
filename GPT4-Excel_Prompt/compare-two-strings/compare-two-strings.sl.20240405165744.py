# Start time: 2024-04-05 17:03:18.224930

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if both the first and second inputs match exactly, including capitalization, return true, else false, and input as ['apple', 'apple'] output is true, input as ['orange', 'Orange'] output is false, input as ['peach', 'peach'] output is true, input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function as per the given specifications
def generated_function(first_input, second_input):
    # Compare the two inputs with exact match including capitalization
    if first_input == second_input:
        return True
    else:
        return False

# Test cases as per the prompt
generated_function('apple', 'apple')  # Expected output: True
generated_function('orange', 'Orange')  # Expected output: False
generated_function('peach', 'peach')  # Expected output: True
generated_function('cherry', 'cherrY')  # Expected output: False
print(generated_function("apple", "apple"))  ## Output: true
print(generated_function("orange", "Orange"))  ## Output: false
print(generated_function("peach", "peach"))  ## Output: true
print(generated_function("cherry", "cherrY"))  ## Output: false

# End time: 2024-04-05 17:03:22.220813
# Elapsed time in seconds: 3.9958058669999446